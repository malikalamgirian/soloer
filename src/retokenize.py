import spacy


# Retokenize to set proper token boundaries using spaCy
def retokenize(doc, entity, entity_indices):
    with doc.retokenize() as retokenizer:
        if len(entity_indices) > 1:
            start_index = entity_indices[0]
            end_index = entity_indices[len(entity_indices) - 1]
            retokenizer.merge(doc[start_index:end_index], attrs={"LEMMA": str(entity)})

            print("\nEntity : ", entity)
            print("\nEntity_indices : ", entity_indices)
            print("\nEntity_index0 : ", str(entity_indices[0]))
            print("\nEntity_index N-1 : ", str(entity_indices[len(entity_indices) - 1]))
#           print("After retokenization : ", [token.text for token in doc])
