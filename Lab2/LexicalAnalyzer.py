import re


def get_reserved(reserved_file):
    reserved = []
    f = open(reserved_file, "r")
    for x in f:
        if is_identifier(x):
            reserved.append(x.split('\n')[0])
    f.close()
    return reserved


def is_identifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){0,10}$', token) is not None


def is_constant(token):
    return re.match('^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None


def get_string_token(sequence, index):
    token = ''
    quote_count = 0
    while index < len(sequence) and quote_count < 2:
        if sequence[index] == '"':
            quote_count += 1
        token += sequence[index]
        index += 1
    return token, index


class LexicalAnalyzer:
    def __init__(self, reserved_file):
        self.reserved = get_reserved(reserved_file)

        self.separators = [",", ";", " ", "(", ")", "{", "}", "]", "["]
        self.sep_without_blank = [",", ";", "(", ")", "{", "}", "]", "["]
        self.operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
                          '>>', '<<', '==', '&&', '||', '!', '!=', '&',
                          '|', '^']
        self.all = ['identifier', 'constant'] + self.sep_without_blank + self.operators + self.reserved

    def is_part_of_operator(self, char):
        for op in self.operators:
            if char in op:
                return True
        return False

    def get_operator_token(self, sequence, index):
        token = ''
        while index < len(sequence) and self.is_part_of_operator(sequence[index]):
            token += sequence[index]
            index += 1
        return token, index

    def break_down_sequence(self, sequence):
        token = ''
        index = 0
        while index < len(sequence):
            if sequence[index] == '"':
                if token:
                    yield token
                token, index = get_string_token(sequence, index)
                yield token
                token = ''

            elif self.is_part_of_operator(sequence[index]):
                if token:
                    yield token
                token, index = self.get_operator_token(sequence, index)
                yield token
                token = ''

            elif sequence[index] in self.separators:
                if token:
                    yield token
                token, index = sequence[index], index + 1
                if token != " ":
                    yield token
                token = ''
            else:
                token += sequence[index]
                index += 1

        if token:
            yield token

    def detect(self, x):
        sequences = x.split("\n")
        for sequence in sequences:
            if sequence:
                for token in self.break_down_sequence(sequence):
                    if token:
                        yield token.split("\n")[0]

    def analyze(self, text):
        f = open(text, "r")
        tokens = []
        line_no = 1
        for x in f:
            for token in self.detect(x):
                if token:
                    tokens.append((token.strip(), line_no))
            line_no += 1
        f.close()
        return tokens
