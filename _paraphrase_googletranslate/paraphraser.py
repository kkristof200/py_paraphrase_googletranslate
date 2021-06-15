# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Union, List, Dict
import random

# Pip
from google_trans_new import google_translator

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: Paraphraser ------------------------------------------------------ #

class Paraphraser:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        input_language: str = 'en',
        secondary_language: str = 'es',
        proxies: Optional[List[Dict[str, str]]] = None,

        # Left these so it won't break based on code based on older versions of this library
        *args,
        **kwargs
    ):
        """Initializer

        Args:
            input_language (str, optional): input/output language. Defaults to 'en'.
            secondary_language (str, optional): The language to use to translate to/from. Defaults to 'es'.
            proxies (Optional[List[Dict[str, str]]], optional): Proxy to use (if a List is passed, it  will be chosen randomly). Defaults to None.
                    format: proxies={
                        'http': 'http_proxy',
                        'https': 'https_proxy',
                    }
        """
        self.input_language = input_language
        self.secondary_language = secondary_language
        self.proxies = [proxies] if isinstance(proxies, dict) else proxies


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def paraphrase(
        self,
        string: str,

        # Left this so it won't break based on code based on older versions of this library
        *args,

        input_language: Optional[str] = None,
        secondary_language: Optional[str] = None,
        proxies: Optional[List[Dict[str, str]]] = None,

        # Left this so it won't break based on code based on older versions of this library
        **kwargs
    ) -> Optional[str]:
        input_language = input_language or self.input_language
        secondary_language = secondary_language or self.secondary_language
        proxies = proxies or self.proxies
        proxies = [proxies] if isinstance(proxies, dict) else proxies

        try:
            return self.__translate(
                s=self.__translate(
                    s=string,
                    src_lang=input_language,
                    dest_lang=secondary_language,
                    proxy=random.choice(proxies) if proxies else None
                ),
                src_lang=secondary_language,
                dest_lang=input_language,
                proxy=random.choice(proxies) if proxies else None
            )
        except:
            return None


    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    @staticmethod
    def __translate(
        s: str,
        src_lang: str,
        dest_lang: str,
        proxy: Optional[Dict[str, str]]
    ) -> str:
        return google_translator(proxies=proxy).translate(s, lang_src=src_lang, lang_tgt=dest_lang)


# -------------------------------------------------------------------------------------------------------------------------------- #