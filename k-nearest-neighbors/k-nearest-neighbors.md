# K-nearest Neighbors

> The k-nearest-neighbors (KNN) algorithm can be used for classification. The algorithm itself is quite simple but useful.
> Often if you are trying to classify something you should consider trying KNN first.

## Feature extraction

Suppose you want to build a recommendation system for netflix.
You have a set of users and want to recommend movies they are most likely to enjoy.
The first step to doing this is to convert the users into a set of numbers. When users sign up to Netflix, they have to rate some cateogries of movies based on how much they like those categories.
For each user, you have a set of ratings.
In this example each user is represented by five numbers (this can be extended to whatever number you like) representing how much they like the categories (Comedy, Action, Drama, Horror and Romance).

To calculate the distance between different users you can use the Pythagorean formula $c = \sqrt{a^2 + b^2}$.
This formula can be extended to any number of numbers (in the exaple five):

$$
distance = \sqrt{(a_1 - a_2)^2 + (b_1 - b_2)^2 + (c_1 - c_2)^2 + (d_1 - d_2)^2 + (e_1 - e_2)^2}
$$

The arrays representing the different people are often called vectors (especially in the context of machine learning).

If you find two similar users using this formula (small distance) you can recommend movies one user likes to the other user (you build a simple recommendation system).
Netflix often asks you to rate movies, the more movies you rate, the better your recommendations will be.

## Regression

Suppose you want to do more than just recommend a movie: you want to guess how a user will rate the movie.
For this take the five people closest to her (using the distance formula).

You could take the average of the ratings the five users closest to the specific user gave (this is called regression).

There are two basic things you'll do with KNN - classification and regression:
- Classification: Categorization into a group
- Regression: Predicting a response

Regression is very useful in different situations.

> **Cosine Similarity**:<br>
> So far you've been using the distance formula to compare the distance between two users.
> A common formula used in practice is cosine similarity. Supose two users are similar, but one is more conservative in their ratings.
> If you keep using hte distance formula, these two users might not be each other's neighbors, even tough they have similar taste.
> Cosine similarity doesn't measure the distance between two vectors, instead itt compares the angles fo the two vectors. It is better at dealing with cases like this.


## Picking good features

To figure out recommendations, you have to find a certain features to represent them with (in the Netflix example it was their ratings for different movie categories).
When you are working with KNN it is really important to pick the right features to compare against. Picking the right features means:
- Features that directly correlate to the taks at hand
- Features that don't have a bias 8for example, if you ask the sers to only rate comedy movies - this doesn't tell you whether they like action movies)


## OCR (Optical character recognition)

> Optical character recognition means you can take a photo of a page oftext, and your computer will read the text for you. Google uses OCR to digitize books. 

You can use KNN for this:
- Go through a lot of images of numbers and extract features of those numbers.
- When you get a new image, extract the features of that image and see what its nearest neighbors are!

Generally speaking the OCR algorithms measure lines, points and curves.


