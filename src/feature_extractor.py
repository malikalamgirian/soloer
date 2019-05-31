import spacy
import detokenize
import retokenize

nlp = spacy.load('en_core_web_sm')
input_instance = {'tokens': ['Downing', 'House', 'is', 'a', 'historic', 'home', 'located', 'at', 'Memphis', ',',
                             'Scotland', 'County', ',', 'Missouri', '.'], 'h': ['memphis', 'Q962034', [[8]]],
                  't': ['scotland county, missouri', 'Q496971', [[10, 11, 12, 13]]]}
input_tokens_list = input_instance["tokens"]

input_head = input_instance['h']
head_entity = input_head[0]
head_entity_id = input_head[1]
head_entity_indices = input_head[2][0]

input_tail = input_instance['t']
tail_entity = input_tail[0]
tail_entity_id = input_tail[1]
tail_entity_indices = input_tail[2][0]

# form a sentence from token list using NLTK
sentence = detokenize.detokenize(input_tokens_list)

print("\nInput tokens list: " + str(input_tokens_list))
print("\nHead: " + str(head_entity))
print("\nTail: " + str(tail_entity))
print("\nNLTK Detokenized Sentential form: " + sentence + "\n")


# Apply spiCy
doc = nlp(str(sentence))


# Re-tokenize
print("\n" + "# Re-tokenize")

retokenize.retokenize(doc, head_entity, head_entity_indices)
print("After head re-tokenization : ", [token.text for token in doc])

retokenize.retokenize(doc, tail_entity, tail_entity_indices)
print("After tail re-tokenization : ", [token.text for token in doc])

# POS
print("\n" + "# POS" + "\n")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)



# Dependency Parsing
print("\n" + "# Dependency Parsing")

## Noun Chunks
print("\n" + "## Noun Chunks" + "\n")
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)

## Parse Tree
print("\n" + "## Parse Tree" + "\n")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])



# Named Entity Recognition NER
print("\n" + "# Named Entity Recognition NER")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)



# Document labels
print("\n" + "# Document labels")
print(doc.cats)
