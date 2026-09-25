# 🚲 Case Study: Cyclistic Bike-Share Analysis

This project represents the final case study for the [Google Data Analytics Professional Certificate](https://grow.google/certificates/data-analytics/).

**Tools used:** Python (Pandas), GitHub, [To be determined: Tableau / PowerBI / Matplotlib]

---

## 1. Ask (Defining the Problem)

**The Situation:** Cyclistic is a bike-share company in Chicago. The director of marketing believes the company’s future success depends on maximizing the number of annual memberships.
**Business Question:** How do annual members and casual riders use Cyclistic bikes differently?
**My Objective:** To analyze historical bike trip data to identify trends and provide data-driven recommendations for a new marketing strategy.

## 2. Prepare (Data Source)

- **Source:** The data has been made available by Motivate International Inc. under [this license](https://ride.divvybikes.com/data-license-agreement).
- **Timeframe:** The last 12 months of historical trip data (CSV format). At the time of the analysis: Sept '25 - Aug '26
- **Organization:** Raw data is stored locally and ignored on GitHub via `.gitignore` due to large file sizes.

## 3. Process (Data Cleaning and Manipulation)

- **Cleaning steps performed:**
  - uniting all the data from different months
  - getting rid of data that was considered incomplete (i.e. the station string was empty)
  - getting rid of flawed data (i.e. the duration of the ride was negative)
- **Full Script:** 01_process.py

## 4. Analyze

- **What is the average ride length for members vs. casual riders?**
  After analyzing the data, we can clearly see in the 'visualizations/mean_duration_of_courses' chart that members usually go for a bike ride which lasts around 12 minutes and the casuals' 20.
- **What is the most popular day of the week for each group?**
  The most popular day of the week for **members** is **Tuesday**, where we can see a **trend** that tells the story about how in the work days bikes are being more used by members, and for **casuals** it's **Saturday**, the **trend** for them suggesting they use our service in the weekends, for recreation.

## 5. Share (Visualizations)

- They can be found in the **visualizations folder**

## 6. Act (Business Recommendations)

After some thoughts, I came up with two possible solutions:

- **Marketing campaign** which encourages people to switch from comuting to work during the week with a bike, instead of a car. This includes ads, tiktoks and some billboards.
- Creating a **new 'middle' type of subscription** so the jump from one another wouldn't seem as big at is seems righ now. For example: following the trend, we could introduce a subscription that focuses on recreational users, including only the weekends (Friday, Saturday and Sunday)
