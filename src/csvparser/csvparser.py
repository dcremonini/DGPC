from src.degiro import CSV_HEADER_NL
from src.language.language import Languages


class LanguageDetector:

    def getLanguageFromHeader(csvHeader: str):
        if csvHeader == CSV_HEADER_NL:
            return Languages.NL
        else:
            raise ValueError(f"The header '{csvHeader}' cannot be managed")
