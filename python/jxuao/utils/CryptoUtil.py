#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64

try:
    from Crypto.Cipher import AES # from pycrypto
except ImportError:
    from crypto.Cipher import AES # from pycryptodome


class Padding:
    @staticmethod
    def pkcs7padding(text):
        """
        明文使用PKCS7填充
        最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
        :param text: 待加密内容(明文)
        :return:
        """
        bs = AES.block_size  # 16
        length = len(text)
        bytes_length = len(bytes(text, encoding='utf-8'))
        # tips：utf-8编码时，英文占1个byte，而中文占3个byte
        padding_size = length if bytes_length == length else bytes_length
        padding = bs - padding_size % bs
        # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
        padding_text = chr(padding) * padding
        return text + padding_text

    @staticmethod
    def pkcs7unpadding(text):
        """
        处理使用PKCS7填充过的数据
        :param text: 解密后的字符串
        :return:
        """
        length = len(text)
        unpadding = ord(text[length - 1])
        return text[0:length - unpadding]


class AesUtil:

    @staticmethod
    def cbc_encrypt(text, key, iv):
        """
        AES加密
        模式cbc
        填充pkcs7
        :param text:
        :param key: 密钥
        :param iv:
        :return:
        """
        key_bytes = bytes(key, encoding='utf-8')
        iv_bytes = bytes(iv, encoding='utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        # 处理明文
        content_padding = Padding.pkcs7padding(text)
        # 加密
        encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
        # 重新编码
        result = base64.b64encode(encrypt_bytes).decode('utf-8')
        return result

    @staticmethod
    def cbc_decrypt(text, key, iv):
        """
        AES解密
        模式cbc
        去填充pkcs7
        :param text:
        :param key:
        :param iv:
        :return:
        """
        key_bytes = bytes(key, encoding='utf-8')
        iv_bytes = bytes(iv, encoding='utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        # base64解码
        encrypt_bytes = base64.b64decode(text)
        # 解密
        decrypt_bytes = cipher.decrypt(encrypt_bytes)
        # 重新编码
        result = decrypt_bytes.decode('utf-8')
        # result = str(decrypt_bytes, encoding='utf-8')
        # 去除填充内容
        result = Padding.pkcs7unpadding(result)
        return result
