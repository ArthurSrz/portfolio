---
{"dg-publish":true,"permalink":"/prototypes/data-position-studio/","tags":["product"]}
---

# Design rationale

#### Why a Data Position ?

One "data position" is a tool made for categorizing people based on their data related skills and profile. It is generally used to create groups with a balanced distribution of skills. For example, to constitute teams with at least one technical profile, you need to identify who has technical skills and then distribute them accordingly. 

As a result, one data position is usually made of : 
* one grid of questions
* responses with associated "scores" to measure skills level 
* some reasoning to allocate profiles in a balanced manner

#### What general concepts behind the Data Position ?

A data position is simply two interrelated things :
1. one colorizer
2. one gatherizer
3. one dispenser

Interrelated because the dispenser will use some *dispensing function* based on the allocated color. Such as :

> [!quote]
> In every group I want 2 blue, 1 red and 3 yellows

Each bubble (representing a person) will be colorized accordingly to some established rules as well. 


> [!question] What are the concepts to understand ? 
> Skill-related questions 
> Hash-table, index table to allocate scores to each response to the questions
> Algorithm (round robin)

# Demo instance of the Data Position Studio

![Screenshot 2024-02-13 at 16.19.14.png|left|300](/img/user/Screenshot%202024-02-13%20at%2016.19.14.png)




<div class="container">  
  <div class="center">  
    <button onclick="window.open('https://forgedatapositionfinal.streamlit.app/', '_blank');">Here</button>  
  </div>  
</div>





