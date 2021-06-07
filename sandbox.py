from PDF_parser import SuperKeywordFinder

kf = SuperKeywordFinder('keywords.txt')
pdfs, pdf_total_matches, pdf_matches = kf.main()
