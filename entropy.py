import math
import numpy as np
from collections import Counter

def get_char_frequencies(domain):
    """Counts character frequencies in a given string."""
    return dict(Counter(domain))

def shannon_entropy(labels, base=2):
    """Computes the Shannon entropy of a given string."""
    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    # Count character occurrencesx
    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.
    for i in probs:
        ent -= i * math.log(i, base)

    return ent

def relative_entropy(observed_freqs, expected_probs):
    N = sum(observed_freqs.values())  # Total number of characters in observed data
    observed_probs = {char: freq / N for char, freq in observed_freqs.items() if freq > 0}

    kl_divergence = sum(
        observed_probs[char] * math.log2(observed_probs[char] / expected_probs[char])
        for char in observed_probs if char in expected_probs and expected_probs[char] > 0
    )

    return kl_divergence

# Test domains
domains = ["google", "microsoft", "uvg", "uspsxcjmvb", "uspsn-tn-track"]

# Given probability distribution
probabilities = {
    '-': 0.013342298553905901, '_': 9.04562613824129e-06, '0': 0.0024875471880163543,
    '1': 0.004884638114650296, '2': 0.004373560237839663, '3': 0.0021136613076357144,
    '4': 0.001625197496170685, '5': 0.0013070929769758662, '6': 0.0014880054997406921,
    '7': 0.001471421851820583, '8': 0.0012663876593537805, '9': 0.0010327089841158806,
    'a': 0.07333590631143488, 'b': 0.04293204925644953, 'c': 0.027385633133525503,
    'd': 0.02769469202658208, 'e': 0.07086192756262588, 'f': 0.01249653250998034,
    'g': 0.038516276096631406, 'h': 0.024017645001386995, 'i': 0.060447396668797414,
    'j': 0.007082725266242929, 'k': 0.01659570875496002, 'l': 0.05815885325582237,
    'm': 0.033884915513851865, 'n': 0.04753175014774523, 'o': 0.09413783122067709,
    'p': 0.042555148167356144, 'q': 0.0017231917793349655, 'r': 0.06460084667060655,
    's': 0.07214640647425614, 't': 0.06447722311338391, 'u': 0.034792493336388744,
    'v': 0.011637198026847418, 'w': 0.013318176884203925, 'x': 0.003170491961453572,
    'y': 0.016381628936354975, 'z': 0.004715786426736459
}

for domain in domains:
    freqs = get_char_frequencies(domain)
    entropy = shannon_entropy(list(domain))  # Pass domain as a list of characters
    relative_ent = relative_entropy(freqs, probabilities)
    
    print(f"Domain: {domain}")
    print(f"  Shannon Entropy: {entropy:.4f}")
    print(f"  Relative Entropy (KL Divergence): {relative_ent:.4f}")
    

# Referencias 
# https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
# ChatGPT
# 