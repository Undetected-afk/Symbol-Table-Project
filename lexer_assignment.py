import re

# Source code sample (test data)
source_code = [
    'let x = 10;',
    'let name = "Alice";',
    'function add(a, b) {',
    '    return a + b;',
    '}',
    'if (x > 5) {',
    '    print("Greater than 5");',
    '} else {',
    '    print("Less than or equal to 5");',
    '}',
    'while (x < 10) {',
    '    x = x + 1;',
    '}',
    '// This is a comment line',
    'let x = 15; // Duplicate variable'
]

# Reserved words and operators defined by the language
reserved_words = {'let', 'function', 'return', 'if', 'else', 'print', 'while'}
data_types = set()  # Not explicitly defined in your language
operators_set = {'+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=', '=',}

# Token categorization
def tokenize(lines):
    literals = set()
    operators = set()
    variables = set()
    reserved = set()
    duplicates = set()
    declared_vars = set()
    
    token_specification = [
        ('LITERAL', r'\b\d+\b|"(.*?)"'),  # integers or strings
        ('OPERATOR', r'==|!=|<=|>=|[+\*/%=<>-]'),  # arithmetic and comparison
        ('IDENTIFIER', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),  # variable/function names
    ]
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
    line_count = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('//') or stripped == '':
            continue  # skip comments and empty lines
        line_count += 1
        for mo in re.finditer(tok_regex, line):
            kind = mo.lastgroup
            value = mo.group()

            if kind == 'LITERAL':
                literals.add(value)
            elif kind == 'OPERATOR':
                if value in operators_set:
                    operators.add(value)
            elif kind == 'IDENTIFIER':
                if value in reserved_words:
                    reserved.add(value)
                elif value in declared_vars:
                    duplicates.add(value)
                    variables.add(value)
                elif value not in reserved_words:
                    declared_vars.add(value)
                    variables.add(value)

    return {
        'literals': literals,
        'operators': operators,
        'variables': variables,
        'duplicates': duplicates,
        'reserved': reserved,
        'data_types': data_types,
        'line_count': line_count
    }

# Remove comments and blank lines for line count
def remove_comments(lines):
    cleaned = []
    for line in lines:
        code_part = line.split('//')[0].strip()
        if code_part:
            cleaned.append(code_part)
    return cleaned

# Generate the lexer report
def generate_report(data):
    print("\n--- Lexer Report ---")
    print(f"Literals ({len(data['literals'])}): {', '.join(data['literals'])}")
    print(f"Operators ({len(data['operators'])}): {', '.join(data['operators'])}")
    print(f"Variables ({len(data['variables'])}): {', '.join(data['variables'])}")
    print(f"Duplicate Variables: {', '.join(data['duplicates']) if data['duplicates'] else 'None'}")
    print(f"Reserved Words ({len(data['reserved'])}): {', '.join(data['reserved'])}")
    print(f"Data Types ({len(data['data_types'])}): {', '.join(data['data_types']) if data['data_types'] else 'None'}")
    print(f"Lines Processed (excluding comments): {data['line_count']}")

if __name__ == '__main__':
    cleaned_lines = remove_comments(source_code)
    token_data = tokenize(cleaned_lines)
    generate_report(token_data)