import itertools
from pdfminer import high_level
import os
import re


class SuperKeywordFinder:
    """
    The Keyword Finder searches for all defined keywords in all available PDFs and produces
    a Report file with its findings.
    """

    def __init__(self, file_with_keywords):
        self.file_with_keywords = file_with_keywords

    def get_pdfs(self):
        """
        Input - PDFs in folder
        Gets all names of PDFs in folder
        Output - list of PDFs in folder names
        """
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        pdfs = []
        for f in files:
            if '.pdf' in f:
                pdfs.append(f)
        assert len(pdfs) == len(set(pdfs)), "PDF names are not unique."  # check that names are unique
        return pdfs

    def drop_diacritics(self, x):
        """
        Input - string
        Replaces all czech diacritics to plain letters
        Output - string without diacrtics
        """
        x = x.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o')\
            .replace('ú', 'u').replace('ů', 'u').replace('ě', 'e').replace('š', 's')\
            .replace('č', 'c').replace('ř', 'r').replace('ž', 'z').replace('ý', 'y')\
            .replace('ť', 't').replace('é', 'e').replace('ď', 'd').replace('ň', 'n')\
            .replace('ä', 'a').replace('ĺ', 'l').replace('ľ', 'l') \
            .replace('ô', 'o').replace('ŕ', 'r')
        return x

    def get_list_of_key_words(self):
        """
        Input - txt file with keywords
        Exctracts keywords from txt file
        Output - list of keywords
        """
        txt_file = open(self.file_with_keywords, encoding='utf8')

        # split by comma
        words = []
        for line in txt_file:
            word = re.split(',| |-', line)
            words.append(word)

        # words formatting
        words = list(itertools.chain.from_iterable(words))
        words = [self.drop_diacritics(x.lower()) for x in words]

        # replace parenthesis and slashes
        words = [w.replace('(', '').replace(')', '').replace('/', '').replace('\\', '') for w in words]
        # replace new line
        words = [x for x in words if x not in ('\n', ' \n', '\n ', '')]
        words = list(set([x.strip() for x in words]))  # only unique words

        return words

    def delete_report_if_exists(self):
        """
        Input - Report file if exists
        Delete Report file
        Output - deleted Report file if existed
        """
        if os.path.isfile('Report.txt'):
            os.remove('Report.txt')

    def pdf_to_words(self, pdf):
        """
        Input - PDF document
        Parses PDF into lower case words
        Output - list of lower case words
        """
        document = high_level.extract_text(pdf, codec='uft-8')
        document = document.replace(u'\xa0', u' ')  # wrong space for correct space
        document = document.replace(u'\n', u' ')  # space instead of new line
        document = document.lower()
        document = self.drop_diacritics(document)
        document_in_list_of_words = document.split(" ")

        def concat_words_with_hyphen(list_of_words):
            """
            Input all words from document
            Find word tthat ends with hypthon and then concatenates it to the next one - division of words on 2 lines
            Outputs newly created words
            """
            additional_concatenated_words = []
            for i in range(len(list_of_words)):
                # if we are no in last word
                if len(list_of_words) != (i + 1):
                    first_word = list_of_words[i]
                    second_word = list_of_words[i + 1]
                    # if word hav more than 2 letters and ends with hyphen
                    if len(first_word) >= 2 and first_word[-1] == "-":
                        new_word = (first_word + second_word).replace("-", "")
                        additional_concatenated_words.append(new_word)
            return additional_concatenated_words

        # add newly created words (concatenated words from two lines) to all words from document
        additional_words = concat_words_with_hyphen(document_in_list_of_words)
        for y in additional_words:
            document_in_list_of_words.append(y)

        return document_in_list_of_words

    def main(self):
        """
        Main function for running whole logic
        """
        pdfs = self.get_pdfs()
        keywords = self.get_list_of_key_words()
        self.delete_report_if_exists()

        pdf_total_matches = {}  # save total count of matches for each pdf
        pdf_matches = {}  # for each pdf saves words and counts. example {pdf_name:{keyword1: 20, keyword2: 10}}
        for pdf in pdfs:
            pdf_parsed_to_words = self.pdf_to_words(pdf)

            no_of_found_matches = 0
            found_words_and_counts = {}

            for keyword in keywords:
                specific_word_counter = 0

                for i in pdf_parsed_to_words:
                    if keyword in i:
                        no_of_found_matches += 1
                        specific_word_counter += 1

                found_words_and_counts[keyword] = specific_word_counter

            # remove zero matches from list
            found_words_and_counts = {k: v for k, v in found_words_and_counts.items() if v != 0}

            # save total number of matches of pdf. Key is pdf name, value is total count of matches for all words.
            pdf_total_matches[pdf] = no_of_found_matches
            # for each pdf save all keywords and count. Key is pdf name, value is another dict. Key is keyword, value
            # is count. Example {pdf_name:{keyword: 20}}
            pdf_matches[pdf] = found_words_and_counts

        return pdfs, pdf_total_matches, pdf_matches


if __name__ == "__main__":
    kf = SuperKeywordFinder('keywords.txt')
    pdfs, pdf_total_matches, pdf_matches = kf.main()

    with open('Report.txt', 'a') as f:
        cntr = 1
        for pdf in pdfs:
            if cntr != 1:
                f.write('\n' + '=====================' + '\n')
            # write total number of matches in pdf
            f.write('Dokument: ' + pdf + '; ' + 'Pocet_nalezu: ' + str(pdf_total_matches[pdf]) + '\n')
            # for each word and its count, write result
            for specific_word, word_count in pdf_matches[pdf].items():
                f.write(specific_word + '(' + str(word_count) + 'x), ')
            cntr += 1
