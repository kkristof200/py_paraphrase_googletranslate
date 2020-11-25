# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Union, List

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: Paraphraser ---------------------------------------------------------- #

class Paraphraser:

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        input_language: str = 'en',
        secondary_language: str = 'es',
        random_ua: bool = False,
        user_agent: Optional[str] = None
    ):
        self.input_language = input_language
        self.secondary_language = secondary_language
        self.random_ua = random_ua
        self.user_agent = user_agent


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    def paraphrase(
        self,
        string: str,
        input_language: Optional[str] = None,
        secondary_language: Optional[str] = None,
        random_ua: Optional[bool] = None,
        user_agent: Optional[str] = None
    ) -> Optional[str]:
        input_language = input_language or self.input_language
        secondary_language = secondary_language or self.secondary_language
        random_ua = random_ua or self.random_ua

        try:
            return self.__translate(
                self.__translate(
                    string, input_language, secondary_language, random_ua, user_agent=user_agent or self.user_agent
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
        random_ua: bool,
        user_agent: Optional[str] = None
    ) -> str:
        from googletrans import Translator
        from googletrans.constants import DEFAULT_USER_AGENT

        ua = user_agent or DEFAULT_USER_AGENT

        if random_ua:
            from fake_useragent import UserAgent

            ua = UserAgent().random

        return Translator(user_agent=ua).translate(s, src=src_lang, dest=dest_lang).text


# ---------------------------------------------------------------------------------------------------------------------------------------- #