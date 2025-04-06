import random 

scores = [random.randint(100,201) for _ in range(200)]

unique_scores = [] 

for score in scores: 
    if score not in unique_scores: 
        unique_scores.append(score)
        
# sum of elements 
total = sum(unique_scores)

total = 0 
for score in unique_scores: 
    total += score
    
print(f"Total Score: {total}")

# Maximum element 

greatest = max(unique_scores)
print(f"Highest Score: {greatest}")

greatest = 0 

for score in unique_scores: 
    if score > greatest: 
        greatest = score
        
print(f"Highest Score: {greatest}")
       
