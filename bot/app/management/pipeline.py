
from app.rules.grammar import *
from creating_rules_sempre import *
from categories import *
from pipeline_aux import *

# main pipeline
# note that there will be 2 questions created:
# one for simple grammar, one for sempre grammar
def pipeline(question):
    new_question_sempre = ''
    new_question_grammar = ''
    last_word_sempre = ''
    new_q = []
    date = 0

    # type 0, means using question without currencies
    # type 1, means using question with currencies
    type = 0
    # call initial setup to gather data from database
    # setup_categories()

    # lowercase the question submitted
    lower_question = lowercase_words(question)
    # remove stop words
    q = stop_words(lower_question)

    # see how many words can be matched in a synonym
    matched, words_grammar, words_sempre = get_max_match(q)

    for i in q :

        if i not in matched:

            new_q.append(str(i))

            # if no synonym found, check for word in categories (to make sure the word is valid)
            category = identify_category(i)

            # if the word is not found, test for date expression, if non present abort mission
            if category == '':

                if date == 0:

                    test = get_date_match(new_q)

                    if test != '':
                        date_matches = test[0]
                        days = test[1]
                        date = test[2]

                        if days == '':
                            return None

                        else:
                            # check which word is last word saved
                            if last_word_sempre == 'expire' or last_word_sempre == 'date' or last_word_sempre == 'ndfdate':

                                # create sempre rule for temporal expression
                                if len(date) == 1:
                                    value = date[0]
                                    create_sempre_rule(date[0])

                                elif len(date) == 2:
                                    value = date[0]
                                    value = value + " " + date[1]
                                    create_sempre_rule(date[0])
                                    create_sempre_rule(date[1])

                                # fill in full question
                                new_question_sempre = new_question_sempre + " " + str(value)
                                new_question_grammar = new_question_grammar + " " + str(value)

                                # update last word
                                last_word_sempre = str(value)

                            # same idea as before
                            elif last_word_sempre == 'rollover' or last_word_sempre == 'neartenordays' or last_word_sempre == 'fartenordays' or last_word_sempre == 'stddevrollover' or last_word_sempre == 'fromdays':

                                value = days[0]
                                create_sempre_rule(days[0])

                                new_question_sempre = new_question_sempre + " " + str(value)
                                new_question_grammar = new_question_grammar + " " + str(value)

                                last_word_sempre = str(value)


            # if word is a currency, then change the currency format, so that both queries are created
            elif category == '1':

                # using type to define which sentence to add to
                type = 1
                currency = currency_swap(i)
                new_question_sempre_currency = new_question_sempre + " " + i
                new_question_sempre_currency_2 = new_question_sempre + " " + currency
                new_question_grammar_currency = new_question_grammar + " " + i
                new_question_grammar_currency_2 = new_question_grammar + " " + currency

                last_word_sempre = i


            # add value to new formatted question
            else:

                new_question_sempre = new_question_sempre + " " + i
                new_question_grammar = new_question_grammar + " " + i

                last_word_sempre = i

        else:
            # clean up words left
            if len(words_sempre) != 1:
                popped_sempre = words_sempre.pop(0)
                popped_grammar = words_grammar.pop(0)

            elif len(words_sempre) == 1:
                popped_sempre = words_sempre[0]
                popped_grammar = words_grammar[0]

            # add value to new formatted question
            if type == 0:
                new_question_sempre = new_question_sempre + " " + popped_sempre
                new_question_grammar = new_question_grammar + " " + popped_grammar

                last_word_sempre = popped_sempre
                continue

            # get full questions for both currency pairs
            # one with the original, one with the swapped
            elif type == 1:
                new_question_sempre_currency = new_question_sempre_currency + " " + popped_sempre
                new_question_sempre_currency_2 = new_question_sempre_currency_2 + " " + popped_sempre
                new_question_grammar_currency = new_question_grammar_currency + " " + popped_grammar
                new_question_grammar_currency_2 = new_question_grammar_currency_2 + " " + popped_grammar

                last_word_sempre = popped_sempre
                continue

    if type == 0:
        # send to grammars
        sg = grammar_function(new_question_grammar)
        sm = to_sempre(new_question_sempre)

    elif type == 1:
        # send to grammars
        sg = grammar_function(new_question_grammar_currency), grammar_function(new_question_grammar_currency_2)
        sm = to_sempre(new_question_sempre_currency), to_sempre(new_question_sempre_currency_2)

    return sg, sm
