import random


def make_markov_model(cleaned_stories, n_gram=2):
    markov_model = {}

    # Create n-grams and count transitions
    for i in range(len(cleaned_stories) - n_gram):
        curr_state = tuple(cleaned_stories[i : i + n_gram])
        next_state = cleaned_stories[i + n_gram]

        if curr_state not in markov_model:
            markov_model[curr_state] = {}

        if next_state in markov_model[curr_state]:
            markov_model[curr_state][next_state] += 1
        else:
            markov_model[curr_state][next_state] = 1

    # Calculate transition probabilities
    for curr_state, transitions in markov_model.items():
        total = sum(transitions.values())
        for next_state in transitions:
            markov_model[curr_state][next_state] /= total

    return markov_model


def generate_text(markov_model, n_gram=2, max_length=100, start=None):
    if start is None:
        current_state = random.choice(list(markov_model.keys()))
    else:
        current_state = tuple(start.split())

    generated_text = list(current_state)

    while len(generated_text) < max_length:
        if current_state in markov_model:
            next_state = random.choices(
                list(markov_model[current_state].keys()),
                list(markov_model[current_state].values()),
            )[0]
            generated_text.append(next_state)
            current_state = tuple(generated_text[-n_gram:])
        else:
            break

    return " ".join(generated_text)


# Function to generate a random story with a specified starting seed and limit
def generate_random_story(markov_model, start=None, n_gram=2, limit=100):
    return generate_text(markov_model, n_gram, max_length=limit, start=start)


# Load the cleaned stories
with open("cleaned_stories.txt", "r", encoding="utf-8") as file:
    cleaned_stories = [line.strip() for line in file]


def generate_output(n_gram, input, token_length):
    markov_model = make_markov_model(cleaned_stories, n_gram)

    text_outputs = []
    for _ in range(5):
        text = generate_random_story(markov_model, input, n_gram, token_length)

        generated = " ".join(text.split())

        text_outputs.append(generated)

        other_outputs = "".join(text + "<br />" for text in text_outputs[1:])

    return text_outputs[0], other_outputs


NGRAM_TEXT_GEN_EXAMPLES = [
    [2, "မႂ် သုင်", 10],
    [2, "မႂ် သုင်", 50],
    [3, "မႂ် သုင် ၶႃႈ", 10],
    [2, "ၵိၼ် ၶဝ်ႈ", 10],
    [3, "လိၵ်ႈ လၢႆး တႆး", 10],
    [4, "ပွႆး ပီ မႂ်ႇ တႆး", 20],
]
