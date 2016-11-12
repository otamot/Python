import corenlp
parser = corenlp.StanfordCoreNLP()
json_data = parser.parse("I am Alice.")
