from src.degiro import CSV_HEADER
from src.language.language import Languages


class LanguageDetector:

    def getLanguageFromHeader(csvHeader: str):
        if csvHeader == CSV_HEADER:
            return Languages.NL
        else:
            raise ValueError(f"The header '{csvHeader}' cannot be managed")
