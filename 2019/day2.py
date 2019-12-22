def int_code_program(code):
    code = code.split(',')
    code = [int(x) for x in code]
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    for chunk in chunks(code, 4):
        if (len(chunk) != 4) or (chunk[0] == 99):
            return ','.join([str(x) for x in code])
        op, a, b, c = chunk
        if op == 1:
            code[c] = code[a] + code[b]
        if op == 2:
            code[c] = code[a] * code[b]
    

def int_code_program_with_gravity_assist(code, noun, verb):
    code = code.split(',')
    code = [int(x) for x in code]

    code[1] = noun
    code[2] = verb
    
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    for chunk in chunks(code, 4):
        if (len(chunk) != 4) or (chunk[0] == 99):
            return ','.join([str(x) for x in code])
        op, a, b, c = chunk
        if op == 1:
            code[c] = code[a] + code[b]
        if op == 2:
            code[c] = code[a] * code[b]
