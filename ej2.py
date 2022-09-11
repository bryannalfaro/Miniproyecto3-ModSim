from itertools import product
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#
dice_faces = ['1', '2', '3', '4', '5', '6']

#Assign scores to each face
faces_scores = dict(zip(dice_faces, range(1, 7)))

#Compute overall scores for throwing two faces
omega = {
    (face1, face2): faces_scores[face1] + faces_scores[face2]
    for face1, face2 in product(dice_faces, repeat=2)
}

#Total faces in dice
total_sample_outcomes = len(omega)

#Count frequencies of each value the random variable can assume
frequencies = dict.fromkeys(omega.values(), 0)
for sample_outcome, overall_score in omega.items():
    frequencies[overall_score] += 1

#Compute probabilities
probabilities = pd.DataFrame(
    data=[
        [value, frequency / total_sample_outcomes]
        for value, frequency in frequencies.items()
    ],
    columns=['Calificación total a obtener al lanzar 2 dados', 'Probabilidad']
)

#Plot PMF as barplot
ax = sns.barplot(
    x='Calificación total a obtener al lanzar 2 dados',
    y='Probabilidad',
    data=probabilities,
)

#Show the graph
plt.show()