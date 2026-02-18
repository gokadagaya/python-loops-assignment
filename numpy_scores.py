import numpy as np
#Task 1:Generate and Inspect the Data
print("*****************************Task:1*******************************")
scores=np.random.randint(50,101,size=(5,4))
print(scores)
print("3rd Student in 2nd subject :",scores[2,1])
print("Last 2 students scores:",scores[:-3])
print("First 3 students in sujects 2 &3 only:",scores[:3,1:3])

#Task 2:  Analyze with Broadcasting
print("*****************************Task:2*******************************")
print("Average Scores per subject:", np.round(scores.mean(axis=0),2),)

curve = np.array([5, 3, 7, 2])
curved_scores = np.clip(scores + curve, 0, 100)

print(curved_scores)

print("Best subject score per student :",curved_scores.max(axis=1))

#Task 3:  Normalize and Identify
print("*****************************Task:3*******************************")
row_min = scores.min(axis=1, keepdims=True)
row_max = scores.max(axis=1, keepdims=True)

normalized = (scores - row_min) / (row_max - row_min)
print("Normalized scores shape :",normalized.shape)

max_index = np.argmax(normalized)
row, col = np.unravel_index(max_index, normalized.shape)

print("Student index:", row)
print("Subject index:", col)

high_scores = curved_scores[curved_scores > 90]
print("Scores above 90:", high_scores)

print("****************************END*******************************")


