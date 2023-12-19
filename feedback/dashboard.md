My goal with building the dashboard was to make into an accessible way to easily poke around with all of the things I had examined during my EDA. I began by building the bare-bones version of the graphs: the histogram, the scatterplot, and the barplots looking at region. I wanted users to be able to select any variable or combination of variables and examine them with a glance. 
At first, this was easy: all I had to do was give the users a select box. For the bivariate exploration, I gave them a multi-select box that limited them to two variables. However, since I talked about using logarithms on some of the variables in my first blog post, I figured I should probably give users the chance to explore that. To do that, I added dynamic checkboxes that changed based on the variables selected which changed the series used from the raw data to a logged version of the data.
For the bivariate graphs, I also wanted to allow users to color the dots by region and add a trendline. This was a bit challenging, but once I figured out what the default values were for those fields in plotly's scatterplot function it was as simple as adding another checkbox.

Finally, for the region bar plots, it was a bit challenging to figure out how to use plotly's histogram feature to make barplots, but once that was done it was pretty simply to adapt my code to make what was needed.

Hunter Croxall's feedback: This looks great! I learned a ton from the data and through the way you organized it! It's really awesome! I honestly don't think you should change much of that section👍

James Martindale (my brother who has a terminal case of tech bro) told me over Telegram: 
```
jakey martydart, [12/17/2023 11:12 PM]
dashboard looks good
```
```
jakey martydart, [12/17/2023 11:12 PM]
if you had to add something it would be some pointers on what to look for
```
```
jakey martydart, [12/17/2023 11:12 PM]
but that's basically in the blog posts
```
```
jakey martydart, [12/17/2023 11:12 PM]
so like I said, if you had to add something
```
```
jakey martydart, [12/17/2023 11:13 PM]
also I just now used a bottle brush to clean my hydroflask and it changed my life
```

Isaac Aguilar: Hey William , I really liked your dashboard as a Statistical Analysis tool. You can clearly see the variance of each variable, its distribution, the correlation between two variables, and missing points. I loved it. I would just recommend to add a decription of the purpose of your dashboard te help the audience know what they can expect from the Dashboard. Also, in the Bivariate Exploration I would restrict the ability to select only 2 values. Right now you can select more than two and it breaks the graph. You can put a warning message to state only to select two.


As my brother mentioned, the blog post explains pretty well what to look for and as I don't expect people to look at the dashobard without having seen the blog posts, I left it as it was. I fixed the multiselect tool for the bivariate analysis (I could have sworn it was fine before, though) and added a link to the EDA blog post so that people will be able to know what the dashboard is for.
