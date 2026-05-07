# EN1: References & Data Sources

> Status: Initial compilation. To be expanded during Phase 1.

---

## Core Academic References

### Platform Lifecycle & Network Effects

- Cusumano, M. A., Gawer, A., & Yoffie, D. B. (2019). *The Business of Platforms*. Harper Business.
- Katz, M. L., & Shapiro, C. (1985). Network externalities, competition, and compatibility. *American Economic Review*, 75(3), 424-440.
- Rochet, J. C., & Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European Economic Association*, 1(4), 990-1029.
- Zhu, F., & Iansiti, M. (2012). Entry into platform-based markets. *Strategic Management Journal*, 33(1), 88-106.
- Parker, G., Van Alstyne, M., & Choudary, S. P. (2016). *Platform Revolution*. W.W. Norton.

### Social Media Decline & Enshittification

- Doctorow, C. (2023). "The 'Enshittification' of TikTok." *Pluralistic*. [Blog/essay, widely cited]
- Hargittai, E. (2020). Potential biases in big data: Omitted voices on social media. *Social Science Computer Review*, 38(1), 10-24.
- Perrin, A., & Anderson, M. (various years). "Social Media Use in [year]." *Pew Research Center*.

### Generational Dynamics

- boyd, d. (2014). *It's Complicated: The Social Lives of Networked Teens*. Yale University Press.
- Madden, M. et al. (2013). "Teens, Social Media, and Privacy." *Pew Research Center*.
- Anderson, M. & Jiang, J. (2018). "Teens, Social Media & Technology 2018." *Pew Research Center*.

### Anonymous & Question Platforms

- Correa, D. et al. (2015). The many shades of anonymity: Characterizing anonymous social media content. *ICWSM*.
- Hosseinmardi, H. et al. (2015). Analyzing labeled cyberbullying incidents on the Instagram social network. *SocInfo*.
- Binns, A. (2014). Don't feed the trolls! Managing troublemakers in magazines' online communities. *Journalism Practice*, 6(4), 547-562.

### Relationship Formation Online

- Granovetter, M. S. (1973). The strength of weak ties. *American Journal of Sociology*, 78(6), 1360-1380.
- Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. *Journal of Human Evolution*, 22(6), 469-493.
- Burke, M., & Kraut, R. E. (2014). Growing closer on Facebook: Changes in tie strength through social network site use. *CHI 2014*.
- Altman, I., & Taylor, D. A. (1973). *Social Penetration: The Development of Interpersonal Relationships*. Holt, Rinehart & Winston.

### Content Production & Creator Fatigue

- Barta, S., Belanche, D., Fernández, A., & Flavián, M. (2023). Influencer marketing on TikTok: The effectiveness of humor and followers' hedonic experience. *Journal of Retailing and Consumer Services*.
- Duffy, B. E. (2017). *(Not) Getting Paid to Do What You Love: Gender, Social Media, and Aspirational Work*. Yale University Press.

---

## Data Sources

### Tier 1: Primary (Public, Reliable)

| Source | URL | Data | Format |
|--------|-----|------|--------|
| SEC EDGAR (Meta) | sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001326801 | 10-K, 10-Q filings | HTML/XBRL |
| SEC EDGAR (Snap) | sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001564408 | 10-K, 10-Q filings | HTML/XBRL |
| Pew Research | pewresearch.org/internet/fact-sheet/social-media/ | Annual social media use surveys | PDF/web |
| DataReportal | datareportal.com/reports/ | Annual Global Digital reports | PDF |

### Tier 2: Secondary (Estimates, Media Reports)

| Source | Data | Notes |
|--------|------|-------|
| Sensor Tower (free tier) | App download estimates | Limited free data |
| Statista | Platform MAU compilations | Some free, some paywalled |
| Wikipedia articles | Platform launch/shutdown dates | Verify with primary sources |
| TechCrunch / The Verge archives | Platform lifecycle events | Media reports |
| Wayback Machine | Historical platform pages | For defunct platforms |

### Tier 3: Question Platform Specific

| Platform | Key Data Points | Source |
|----------|----------------|--------|
| Formspring | Launch 2009, Peak ~28M, Shutdown 2013 | TechCrunch, Wikipedia |
| Ask.fm | Launch 2010, Peak ~150M MAU | Company claims, media |
| Sarahah | Launch 2017, 300M downloads | App Annie reports, media |
| Yik Yak | Launch 2013, Shutdown 2017, Revive 2021, Dead 2023 | TechCrunch |
| tbh | Launch 2017, 5M users in 9 weeks, Acquired by FB | TechCrunch |
| Gas | Launch 2022, 10M+ downloads, Acquired by Discord 2023 | TechCrunch |
| NGL | Launch 2022, 15M+ downloads | Sensor Tower, media |
| Curious Cat | ~5M peak | Estimates |

---

## To Collect (Phase 1 Checklist)

### Week 1 (Apr 1-4)

```
□ Meta 10-K (2012-2025): Extract FB DAU, MAU, DAU/MAU ratio by quarter
  → data/meta_quarterly.csv

□ Snap 10-K (2017-2025): Extract DAU, ARPU by quarter
  → data/snap_quarterly.csv

□ Pew Social Media surveys: Compile all available years
  Age groups: 18-29, 30-49, 50-64, 65+
  Platforms: Facebook, Instagram, Snapchat, Twitter, TikTok, YouTube
  → data/pew_social_media.csv
```

### Week 2 (Apr 7-11)

```
□ Question platform lifecycle data: Compile from media reports
  Fields: name, launch_date, peak_date, peak_mau, shutdown_date, cause
  → data/question_platforms.csv

□ DataReportal: Extract global platform MAU (2020-2025)
  → data/global_platform_mau.csv

□ Literature: Collect and read 30+ papers
  → Update this references.md with full citations
```
