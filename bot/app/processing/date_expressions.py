from datetime import datetime, timedelta
from calendar import monthrange
from nlp_processing import *
# import parsedatetime as pdt #pip
import re


# type 1 will give in dates
# type 0 will give in days      Qaaaaa<b
def date_synonyms(expression, type):
    matched = re.search(r"(next|last)\s([0-9\s]*)(day|week|year|quarter)", expression)
    year_request = re.search(r"([0-9]{4})", expression)
    month_year_request = re.search(
        r"(january|february|march|april|may|june|july|august|september|october|november|december)"
        r"| ((january|february|march|april|may|june|july|august|september|october|november|december)([0-9]{4}))",
        expression)
    quick = re.search(r"yesterday|tomorrow|(this year)", expression)

    now = datetime.today()
    formatted_now = "{:%Y-%m-%d}".format(now)

    if quick:

        if quick.group(1) == 'yesterday':
            yesterday = now - timedelta(days=1)

            if type == 1:
                return "{:%Y-%m-%d}".format(yesterday)

            else:
                difference = now.date() - yesterday.date()
                return difference.days

        elif quick.group(1) == 'tomorrow':
            tomorrow = now + timedelta(days=1)

            if type == 1:
                return "{:%Y-%m-%d}".format(tomorrow)

            else:
                difference = tomorrow.date() - now.date()
                return difference.days

        elif quick.group(1) == 'this year':
            first_day = datetime(now.year, 1, 1)
            last_day = datetime(now.year, 12, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = last_day.date() - first_day.date()
                return difference.days

    elif year_request:
        first_day = datetime(int(year_request.group(1)), 1, 1)
        last_day = datetime(int(year_request.group(1)), 12, 31)

        if type == 1:
            return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

        else:
            difference = now.date() - first_day.date()
            return difference.days

    elif month_year_request:

        if month_year_request.group(1) == 'january':

            if month_year_request.group(2):
                year = int(month_year_request.group(2))
                first_day = datetime(year, 1, 1)
                last_day = datetime(year, 1, 31)

            else:
                first_day = datetime(now.year, 1, 1)
                last_day = datetime(now.year, 1, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'february':

            if month_year_request.group(2):
                year = int(month_year_request.group(2))
                first_day = datetime(year, 2, 1)
                last_day = datetime(year, 2, monthrange(now.year, 2)[1])

            else:
                first_day = datetime(now.year, 2, 1)
                last_day = datetime(now.year, 2, monthrange(now.year, 2)[1])

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'march':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 3, 1)
                last_day = datetime(year, 3, 31)

            else:
                first_day = datetime(now.year, 3, 1)
                last_day = datetime(now.year, 3, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'april':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 4, 1)
                last_day = datetime(year, 4, 30)

            else:
                first_day = datetime(now.year, 4, 1)
                last_day = datetime(now.year, 4, 30)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'may':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 5, 1)
                last_day = datetime(year, 5, 31)

            else:
                first_day = datetime(now.year, 5, 1)
                last_day = datetime(now.year, 5, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'june':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 6, 1)
                last_day = datetime(year, 6, 30)

            else:
                first_day = datetime(now.year, 6, 1)
                last_day = datetime(now.year, 6, 30)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'july':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 7, 1)
                last_day = datetime(year, 7, 31)

            else:
                first_day = datetime(now.year, 7, 1)
                last_day = datetime(now.year, 7, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'august':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 8, 1)
                last_day = datetime(year, 8, 31)

            else:
                first_day = datetime(now.year, 8, 1)
                last_day = datetime(now.year, 8, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'september':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 9, 1)
                last_day = datetime(year, 9, 30)

            else:
                first_day = datetime(now.year, 9, 1)
                last_day = datetime(now.year, 9, 30)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'october':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 10, 1)
                last_day = datetime(year, 10, 31)

            else:
                first_day = datetime(now.year, 10, 1)
                last_day = datetime(now.year, 10, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'november':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 11, 1)
                last_day = datetime(year, 11, 30)

            else:
                first_day = datetime(now.year, 11, 1)
                last_day = datetime(now.year, 11, 30)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

        elif month_year_request.group(1) == 'december':

            if month_year_request.group(2):
                year = month_year_request.group(2)
                first_day = datetime(year, 12, 1)
                last_day = datetime(year, 12, 31)

            else:
                first_day = datetime(now.year, 12, 1)
                last_day = datetime(now.year, 12, 31)

            if type == 1:
                return ["{:%Y-%m-%d}".format(first_day), "{:%Y-%m-%d}".format(last_day)]

            else:
                difference = now.date() - first_day.date()
                return difference.days

    elif matched:
        if matched.group(1) == 'next':

            if matched.group(3) == 'day':

                if matched.group(2) != "":
                    number = int(matched.group(2))
                    other = now + timedelta(days=number)

                    if type == 1:
                        return [formatted_now, "{:%Y-%m-%d}".format(other)]

                    else:
                        difference = other.date() - now.date()
                        return difference.days

                else:
                    number = 1
                    other = now + timedelta(days=number)

                    if type == 1:
                        return [formatted_now, "{:%Y-%m-%d}".format(other)]

                    else:
                        difference = now.date() - other.date()
                        return difference.days

            elif matched.group(3) == 'week':

                if matched.group(2) != "":
                    number = int(matched.group(2))
                    other = now + timedelta(weeks=number)

                    if type == 1:
                        return [formatted_now, "{:%Y-%m-%d}".format(other)]

                    else:
                        difference = other.date() - now.date()
                        return difference.days

                else:
                    number = 1
                    other = now + timedelta(weeks=number)

                    if type == 1:
                        return [formatted_now, "{:%Y-%m-%d}".format(other)]

                    else:
                        difference = other.date() - now.date()
                        return difference.days

            elif matched.group(3) == 'year':

                if matched.group(2) != "":
                    number = int(matched.group(2))
                    other = now + timedelta(weeks=number * 52)

                    if type == 1:
                        return [formatted_now, "{:%Y-%m-%d}".format(other)]

                    else:
                        difference = other.date() - now.date()
                        return difference.days

                else:
                    number = 1
                    other = now + timedelta(weeks=number * 52)

                    if type == 1:
                        return [formatted_now, "{:%Y-%m-%d}".format(other)]

                    else:
                        difference = other.date() - now.date()
                        return difference.days

            elif matched.group(3) == 'quarter':
                quarter = calculate_next_quarter(type)
                return quarter

        elif matched.group(1) == 'last':

            if matched.group(3) == 'day':

                if matched.group(2) != "":
                    number = int(matched.group(2))
                    other = now - timedelta(days=number)

                    if type == 1:
                        return ["{:%Y-%m-%d}".format(other), formatted_now]

                    else:
                        difference = now.date() - other.date()
                        return difference.days

                else:
                    number = 1
                    other = "{:%Y-%m-%d}".format(now - timedelta(days=number))
                    return [other, formatted_now]

            elif matched.group(3) == 'week':
                if matched.group(2) != "":
                    number = int(matched.group(2))
                    other = now - timedelta(weeks=number)

                    if type == 1:
                        return ["{:%Y-%m-%d}".format(other), formatted_now]

                    else:
                        difference = now.date() - other.date()
                        return difference.days

                else:
                    number = 1
                    other = now - timedelta(weeks=number)

                    if type == 1:
                        return ["{:%Y-%m-%d}".format(other), formatted_now]

                    else:
                        difference = now.date() - other.date()
                        return difference.days

            elif matched.group(3) == 'year':
                if matched.group(2) != "":
                    number = int(matched.group(2))
                    other = now - timedelta(weeks=number * 52)

                    if type == 1:
                        return ["{:%Y-%m-%d}".format(other), formatted_now]

                    else:
                        difference = now.date() - other.date()
                        return difference.days

                else:
                    number = 1
                    other = now - timedelta(weeks=number * 52)

                    if type == 1:
                        return ["{:%Y-%m-%d}".format(other), formatted_now]

                    else:
                        difference = now.date() - other.date()
                        return difference.days

            elif matched.group(3) == 'quarter':
                return calculate_last_quarter(type)
    else:
        return 0


def calculate_last_quarter(type):
    now = datetime.now()
    quarter = (now.month - 1) / 3 + 1
    last_day_last_quarter = datetime(now.year, 3 * quarter - 2, 1)
    first_day_last_quarter = datetime(last_day_last_quarter.year if last_day_last_quarter.month - 3 >= 0
                                      else last_day_last_quarter.year - 1, (last_day_last_quarter.month - 3) % 12, 1)

    if type == 1:
        return [first_day_last_quarter, last_day_last_quarter]

    else:
        difference = last_day_last_quarter.date() - first_day_last_quarter.date()
        return difference.days


def calculate_next_quarter(type):
    now = datetime.now()
    current_quarter = (now.month - 1) / 3 + 1
    future_quarter = (current_quarter + 4) % 4 + 1
    future_quarter_first = datetime(now.year if future_quarter != 1
                                    else now.year + 1, (current_quarter * 3 + 1) % 12, 1)
    future_quarter_last = datetime(now.year + 1 if (future_quarter == 1) or (future_quarter == 4)
                                   else now.year, (future_quarter * 3 + 1) % 12, 1)

    if type == 1:
        return [future_quarter_first, future_quarter_last]

    else:
        difference = future_quarter_last.date() - future_quarter_first.date()
        return difference.days


def remove_date_expressions(question):
    word_tokens = tokenizing(question)
    stop = ["next", "last", "day", "week", "year", "quarter",
            "january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
            "november", "december", "yesterday", "tomorrow", "this"]

    cleaned_question = []

    for w in word_tokens:
        if w not in stop:
            cleaned_question.append(str(w))

    final_clean = ' '.join([i for i in cleaned_question if not i.isdigit()])

    return final_clean

#if __name__ == '__main__':
 #  test = date_synonyms("january", 1)
  # print(test)
