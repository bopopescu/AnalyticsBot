import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'MEASURE', 'ATTRIBUTE', 'EXCLUDE', 'VALUE', 'COMPARE', 'DATE')

# Tokens
t_MEASURE = r'volume|totaltrades|stddevrolloverdays|spot\sprice\sstrike|rolloverratio|rank|netvolumeratio|netvolume' \
            r'nearlegvolume|latestrolloverdays|ev|cc\stotal|cc\snonrisk|cc\satrisk|averagerolloverdays|maxabsnetvolume'

t_ATTRIBUTE = r'tradestatus|tenor|product\sgroup|product|platform|newtrade|netclientposition|neartenordays|' \
              r'maxfuturedate|marketer|localblotter|leg|fromdays|fartenordays|expiry\sdate|deal\sid|deal\sdate' \
              r'|currencypairgroup|currency\spair|crdscode|client\sdeal\sside|client' \
              r'|broker_fxt|ndf|fixing\sdate'

t_VALUE = r'([a-zA-Z]{3}[/][a-zA-Z]{3})|[a-zA-Z_0-9]+ '

t_DATE = r'([0-9]{4}[-][0-9]{2}[-][0-9]{2})|([0-9]{9})'

# for word exclude
def t_EXCLUDE(t):
    r'exclude'
    return t

# for word compare
def t_COMPARE(t):
    r'highest'
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lex.lex()

# Dictionary of names (for storing variables)
names = {}

# rules for grammar
# statement declares which tokens to be used
# p[0] is the result
# other p[] correspond to the token in the position
def p_statement_date(p):
    '''statement : ATTRIBUTE DATE'''

    p[0] = "".join(
        (
        "SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[1], "]", " = ", " ' ",
        p[2], " ' ",))


def p_statement_attribute_date(p):
    '''statement : ATTRIBUTE ATTRIBUTE DATE
                | MEASURE ATTRIBUTE DATE'''

    p[0] = "".join(
        ("SELECT ", "[", p[1], "]", " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[",
         p[2], "]", " = ", " ' ", p[3], " ' "))


def p_statement_date_date(p):
    '''statement : ATTRIBUTE DATE DATE'''

    p[0] = "".join(
        ("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[1], "]", " >= ",
         " ' ", p[2], " ' ", " AND ",
         "[", p[1], "]", " <= ", " ' ", p[3], " ' "))


def p_statement_attribute_date_date(p):
    '''statement : ATTRIBUTE ATTRIBUTE DATE DATE
                | MEASURE ATTRIBUTE DATE DATE'''

    p[0] = "".join(
        ("SELECT ", "[", p[1], "]", " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[",
         p[2], "]", " >= ", " ' ", p[3], " ' ",
         " AND ",
         "[", p[2], "]", " <= ", " ' ", p[4], " ' "))


def p_statement_single(p):
    ''' statement : MEASURE VALUE
                | ATTRIBUTE VALUE '''

    p[0] = "".join(("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[1], "]",
                    " = ", " ' ", p[2], " ' "))


def p_statement_single_second(p):
    ''' statement : VALUE MEASURE
                | VALUE ATTRIBUTE '''
    p[0] = "".join(("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[2], "]",
                    " = ", " ' ", p[1], " ' "))


def p_statement_exclude(p):
    ''' statement : MEASURE VALUE EXCLUDE
                | ATTRIBUTE VALUE EXCLUDE '''
    p[0] = "".join(("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[1], "]",
                    " != ", " ' ", p[2], " ' "))


def p_statement_exclude_middle(p):
    ''' statement : MEASURE EXCLUDE VALUE
                | ATTRIBUTE EXCLUDE VALUE '''
    p[0] = "".join(("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[1], "]",
                    " != ", " ' ", p[3], " ' "))


def p_statement_exclude_first(p):
    ''' statement : EXCLUDE MEASURE VALUE
                | EXCLUDE ATTRIBUTE VALUE '''
    p[0] = "".join(("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[2], "]",
                    " != ", " ' ", p[3], " ' "))


def p_statement_exclude_large(p):
    ''' statement : MEASURE EXCLUDE ATTRIBUTE VALUE
                | ATTRIBUTE EXCLUDE MEASURE VALUE
                | ATTRIBUTE EXCLUDE ATTRIBUTE VALUE
                | MEASURE EXCLUDE MEASURE VALUE '''
    p[0] = "".join(
        ("SELECT ", "[", p[1], "]", " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[",
         p[3], "]", " != ", " ' ", p[4], " ' "))


def p_statement_multiple_VALUE_second(p):
    ''' statement : ATTRIBUTE VALUE MEASURE
                | MEASURE VALUE ATTRIBUTE
                | ATTRIBUTE VALUE ATTRIBUTE '''
    p[0] = "".join(
        ("SELECT ", "[", p[3], "]", " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[",
         p[1], "]", " = ", " ' ", p[2], " ' "))


def p_statement_multiple_value_third(p):
    ''' statement : ATTRIBUTE MEASURE VALUE
                | MEASURE ATTRIBUTE VALUE
                | ATTRIBUTE ATTRIBUTE VALUE '''
    p[0] = "".join(
        ("SELECT ", "[", p[1], "]", " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[",
         p[2], "]", " = ", " ' ", p[3], " ' "))


def p_statement_multiple_value_four(p):
    ''' statement : ATTRIBUTE VALUE MEASURE VALUE
                | MEASURE VALUE ATTRIBUTE VALUE
                | ATTRIBUTE VALUE ATTRIBUTE VALUE'''
    p[0] = "".join(("SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", "[", p[1], "]",
                    " = ", " ' ", p[2], " ' ",
                    " AND ", "[", p[3], "]", " = ", " ' ", p[4], " ' "))


def p_statement_compare(p):
    ''' statement : ATTRIBUTE COMPARE MEASURE
                | MEASURE COMPARE ATTRIBUTE
                | ATTRIBUTE COMPARE ATTRIBUTE '''
    p[0] = "".join(
        ("SELECT TOP 10 ", "[", p[3], "]", ", ", "[", p[1], "]",
         " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] "))


def p_statement_compare_single(p):
    ''' statement : COMPARE MEASURE
                | COMPARE ATTRIBUTE '''
    p[0] = "".join(
        ("SELECT TOP 10 ", "[", p[2], "]",
         " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] "))


def p_error(p):
    print(p)
    print("Syntax error at '%s'" % p.value)


yacc.yacc()


def grammar_function(question):
    try:
        s = question
    except EOFError:
        pass
    r = yacc.parse(s)
    return str(r)
