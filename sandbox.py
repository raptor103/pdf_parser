from PDF_parser import SuperKeywordFinder

# kf = SuperKeywordFinder('keywords.txt')
# pdfs, pdf_total_matches, pdf_matches = kf.main()
#
# print(pdfs)
# print(pdf_total_matches)
# print(pdf_matches)

kf = SuperKeywordFinder('keywords.txt')
document_in_list_of_words = kf.pdf_to_words("pdf_test1.pdf")
for i in document_in_list_of_words:
    if "pri" in i:
        print(i)
#
# print(pdfs)
# print(pdf_total_matches)
# print(pdf_matches)