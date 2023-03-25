# Metaphone/Doublemetaphone experiments with Norvig SpellChecker
## Based on repo https://github.com/pileyan/webinar_spellchecker by Yan Pile

### Test results on datasets from https://www.kaggle.com/datasets/bittlingmayer/spelling:
#### without `doublemetaphone`:
#####
- spell-testset1.txt: 75% of 270 correct (6% unknown) at 32 words per second 
- spell-testset2.txt: 68% of 400 correct (11% unknown) at 24 words per second 
- wikipedia.txt: 61% of 2455 correct (24% unknown) at 17 words per second 
- aspell.txt: 43% of 531 correct (23% unknown) at 14 words per second 

#### with `doublemetaphone`:
#####

- spell-testset1.txt: 75% of 270 correct (6% unknown) at 32 words per second 
- spell-testset2.txt: ${\color{green}69{\percent}}$ of 400 correct (11% unknown) at 27 words per second 
- wikipedia.txt: 61% of 2455 correct (24% unknown) at 19 words per second 
- aspell.txt: $\qty[color=red]{45}{\percent}$ of 531 correct (23% unknown) at 14 words per second

### To get test results run `python tests.py`