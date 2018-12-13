#### 1. Temperature and air pollution are known to be correlated. We collect data from two laboratories, in Boston and Montreal. Boston makes their measurements of temperature in Fahrenheit, and Montreal in degrees centigrade. Boston measures pollution in particles per cubic yard of air; Montreal uses cubic meters. Both report a correlation of exactly 0.58 between temperature and pollution. Which of the following is true:
  * A. Boston really has the higher correlation, because Fahrenheit temperatures are higher than Centigrade.
  * B. Montreal really has the higher correlation, because cubic meters are bigger than cubic yards.
  * C. Both cities have the same correlation, because correlation is independent of the units of measurement.
  * D. We do not know which city has the really higher correlation.

**Answer:** C. The strength of a correlation does not change if units change by a linear transformation such as:
Fahrenheit = 32 + (5/9) * Centigrade

#### 3. We measure heights and weights of 100 twenty-year old male college students. Which will have the higher correlation:
  * A. corr(height, weight) will be much greater than corr(weight, height)
  * B. corr(weight, height) will be much greater than corr(height, weight)
  * C. Both will have the same correlation.
  * D. Both will be about the same, but corr(weight, height) will be a little higher.
  * E. Both will be about the same, but corr(height, weight) will be a little higher.
**Answer:** C. Correlation is independent of the order in which the variables enter.

#### 4. Two lists of numbers, X and Y, have a correlation of 0.3; X and Z have a correlation of - 0.7
We know that:
  * A. the stronger correlation is the correlation of X and Y, since it is positive.
  * B. the stronger correlation is the correlation of X and Z.
  * C. the two correlations are equally strong, since 1.0 - 0.7 = 0.3
  * D. We cannot tell which is stronger without more information.
Answer: B. The stronger correlation is determined by the absolute value, since it measures the scatter of points
about a line. Whether the line has a positive or negative slope, the less the scatter, the greater the absolute value
of the correlation.

#### 5. Suppose men always married women who were 10 percent shorter than they were. The correlation coefficient of the heights of married couples would be:
  * A. 0.10 if the correlation were computed with corr(male.height, female.height)
  * B. -0.10 if the correlation were computed with corr(female.height, male.height)
  * C. 0.10 no matter which way the correlation were computed.
  * D. 1.0 since the height of the man is always predictable from the height of the woman.
Answer: D. All points in a graph of the correlation would line on the straight line Hf = 0.9 * Hm
where Hf = female height and Hm = male height.

#### 6. In one class, the correlation between the final and the midterm was 0.5, whereas the correlation between the final and the homework grades was 0.25. This means that:
  * A. the relation of the final and the midterm was twice as linear as the relation between the final and the
homework.
  * B. the relation of the final and the homework was twice as linear as the relation between the final and the
midterm.
  * C. More of the variation of the final was explained by the homework grades than by the midterm grades.
  * D. More of the variation of the final was explained by the midterm grades than by the homework grades.
Answer: D. The phrase "more linear" is meaningless; a line is either linear or curved; and correlation is always
correlation around a straight line. It does indicate (when squared) the percentage of the variance explained, and
the midterm grade explained square(.5) = .25 or 25 percent of the variance, where the homework explained only
square(.25) = .0625 or 6.25 percent of the variance.

#### 7. The unemployment rate is related to inflation by the Phillips curve, which is typically a negative sloped curve looking like a hyperbola -- inflation is very high at very low rates of unemployment, and it takes very high rates of unemployment to bring inflation down to zero. We compute a correlation coefficient between unemployment rates and inflation, and find it is negative 0.5. The true relation between the two is most probably:
  * A. exactly as reported by the correlation coefficient.
  * B. stronger than reported by the correlation coefficient, due to the non-linearity.
  * C. weaker than reported by the correlation coefficient, due to the great scatter of points around the line.
Answer: B. The correlation coefficient reports the cluster of points around a straight line; if the true relation is
curvilinear, the correlation will understate the strength of the relation.

#### 8. An investigator is studying the relation between the physical and intellectual growth of primary schoolchildren (grades 1-6). At each grade level, she notes that the correlation between the height of children and the size of their vocabulary is zero. For all students in the school, the correlation is likely to be:
  * A. Positive
  * B. Negative
  * C. About zero
  * D. Cannot tell.
Answer: A. While height and vocabulary size have nothing to do with each other, both have a lot to do with
age, especially for ages 6 to 12. The common cause will lead to a strong correlation of the two, which of course
could not be said of (say) ages 60 to 72.

#### 9. A study is done of students commuting to a large university by bicycle. The correlation between the time spent waiting at traffic lights and total cycling time was 0.50. This means:
  * A. The average rider spent half his cycling time waiting at traffic lights.
  * B. The more time a rider spends waiting at traffic lights, the higher is total time is likely to be.
  * C. If the rider's time at traffic lights increases by 5 minutes, he will spend an additional 10 minutes
commuting, on the average.
  * D. If the rider's time at traffic lights increases by 10 minutes, he will spend an additional 5 minutes
commuting, on the average.
Answer: B. You would need a regression equation to see whether or not time at lights predicted an exact time of
commute. If the distances of the commute varied, using time at lights alone would lead to an omitted variable
problem for a regression of total time on time at lights

#### 10. The correlation between the ages of the husbands and wives in the United States was which of the
following?
  * A. + 1.0 
  * B. + 0.85 
  * C. zero 
  * D. - 0.85 
  * E. -1.0
Answer: B. Men usually marry women of about their own age, but of course there are enough exceptions that
the correlation is not perfect.

#### 11. A study is done of the impact of a drug on body temperature and blood pressure. We have three observations:
Temperature(F) Pressure (mg) Temp - 97 Pressure - 80
99 100 2 20
97 80 0 0
 104 150 7 70
The correlation coefficient is closest to
  * A. + 1.0 
  * B + 0.8 
  * C + 0.5 
  * D. zero 
  * E. -0.5
Hint: a good guess is possible by plotting the data carefully.
 a better one is possible by subtracting the lowest number in each list from all the other numbers in that list.
Answer: A. Transform the first column of data by subtracting 97 from each number; transform the other column
by subtracting 80 from each. The result is given above; the line Pressure = 10*Temp holds perfectly for all
points.

#### 12. The correlation between the average midterm score of each of 10 classes of statistics and the average final exam score was found to be 0.85. A statistics instructor concludes that if a student has a B on the midterm, he has an 85 percent chance of a B on the final. This conclusion is:
  * A. correct
  * B. incorrect, because it is an ecological correlation, which means there is usually much more variance of
individuals than of averages
  * C. incorrect, because it is an average correlation, and there is usually much more variance of averages
than of individuals.
Answer: B. 
