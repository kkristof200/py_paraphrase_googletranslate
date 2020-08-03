# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: Paraphraser ---------------------------------------------------------- #

class Paraphraser:

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        input_language: str = 'en',
        secondary_language: str = 'es',
        random_ua: bool = False
    ):
        self.input_language = input_language
        self.secondary_language = secondary_language
        self.random_ua = random_ua


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    def paraphrase(
        self,
        string: str,
        input_language: Optional[str] = None,
        secondary_language: Optional[str] = None,
        random_ua: Optional[bool] = None
    ) -> Optional[str]:
        input_language = input_language or self.input_language
        secondary_language = secondary_language or self.secondary_language
        random_ua = random_ua or self.random_ua

        try:
            return self.__translate(
                self.__translate(
                    string, input_language, secondary_language, random_ua
                ), secondary_language, input_language, random_ua
            )
        except:
            return None


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    @staticmethod
    def __translate(
        s: str,
        src_lang: str,
        dest_lang: str,
        random_ua: bool
    ) -> str:
        from googletrans import Translator
        from googletrans.constants import DEFAULT_USER_AGENT

        ua = DEFAULT_USER_AGENT

        if random_ua:
            from fake_useragent import UserAgent

            ua = UserAgent().random

        return Translator(user_agent=ua).translate(s, src=src_lang, dest=dest_lang).text


# ---------------------------------------------------------------------------------------------------------------------------------------- #