import random
import item_lists
import re
import visual_layout

# Helper function to choose a random element from a set
def choose_one(s):
    return random.choice(list(s))

def set_descriptor():
    # Choose either a pop culture or item descriptor
    if random.random() < 0.2:
        # Pop culture descriptor
        descriptor = choose_one(item_lists.pop_culture_list) + "-style"
    else:
        descriptor = choose_one(item_lists.descriptors)
    return descriptor

def set_setting(descriptor):
    # Use 'an' if descriptor starts with a vowel sound
    vowels = ("a", "e", "i", "o", "u")
    article = "an" if descriptor[0] in vowels else "a"
    # 75% chance to use article, else use a random phrase from more_than_one or obscure_setting
    if random.random() < 0.5:
        return (article, "")
    else:
        if random.random() > 0.7:
            # Use more_than_one
            return (choose_one(item_lists.more_than_one), "s")
        else:
            # Use obscure_setting
            return (choose_one(item_lists.obscure_setting), "")

def set_object():
    # Pick a random object from items
    return choose_one(item_lists.items)

def set_verb():
    # Choosing a verb
    return choose_one(item_lists.verbs)

def set_format():
    # Choose sentence structure
    if random.random() < 0.9:
        return "{setting} {descriptor} {obj}{plural}"
    else:
        return choose_one(item_lists.sentence_formats)

    

def fill_template_with_randoms(template):
    # Map variable names to their generator functions
    generators = {
        'setting': lambda: set_setting(set_descriptor())[0],
        'descriptor': set_descriptor,
        'obj': set_object,
        'plural': lambda: set_setting(set_descriptor())[1],
        'verb': set_verb
    }
    # Function to handle {choose_one:...} placeholders
    def choose_one_replacer(match):
        options = match.group(1).split(',')
        return random.choice([opt.strip() for opt in options])
    # Replace all {choose_one:...} placeholders first
    template = re.sub(r'\{choose_one:([^}]+)\}', choose_one_replacer, template)
    # For each {var} in the template, replace with a fresh random value
    def replacer(match):
        var = match.group(1)
        if var in generators:
            return str(generators[var]())
        return match.group(0)
    return re.sub(r'\{(\w+)}', replacer, template)

def main():
    sentence_template = set_format()
    sentence = fill_template_with_randoms(sentence_template)
    prompt = f"Draw\n{sentence}."
    def random_prompt():
        t = set_format()
        s = fill_template_with_randoms(t)
        print(f"Draw\n{s}.")
        return f"{s}."
    visual_layout.MainWindow(prompt_text=prompt, prompt_generator=random_prompt).mainloop()

if __name__ == "__main__":
    main()
