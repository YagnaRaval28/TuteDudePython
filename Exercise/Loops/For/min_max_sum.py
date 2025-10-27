scores=[2,15,75,0,0,183,100]
total=0
for score in scores:
    total+=score
print(f"Total score is {total} in {len(scores)} matches")   

highest=scores[0]
for score in scores:
    if highest<score:
        highest=score
print("Highest score is",highest)

lowest=scores[0]
for score in scores:
    if lowest>score:
        lowest=score
print("Lowest score is",lowest)        