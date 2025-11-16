from collections import deque

def forward_chain(rules, facts):

    counts = []
    parsed_rules = []

    inferred = set(facts) # will not preserve order
    agenda = deque(facts)

    # Assuming that a "simple" algorithm only expects 1 or 0 operators (ie. A & B | C => D is an invalid input),
    # and that the predicate only contains one inference (ie. A & B => C | D is invalid
    for rule_str in rules:
        conditions_str, inference = rule_str.split("=>")
        rule_data = {
            'inference': inference.strip(),
            'premises': set()
        }

        if "&" in conditions_str:
            premises = conditions_str.split("&")
            counts.append(len(premises))
            rule_data['premises'] = set(p.strip() for p in premises)
        elif "|" in conditions_str:
            premises = conditions_str.split("|")
            counts.append(1)
            rule_data['premises'] = set(p.strip() for p in premises)
        else:
            counts.append(1)
            rule_data['premises'] = {conditions_str.strip()}
        parsed_rules.append(rule_data)


    while agenda:
        fact = agenda.popleft()

        for i, rule in enumerate(parsed_rules):
            if counts[i] > 0 and fact in rule['premises']:
                counts[i] -= 1

            if counts[i] == 0:
                new_inference = rule['inference']
                if new_inference not in inferred:
                    inferred.add(new_inference)
                    agenda.appendleft(new_inference)

    return inferred
