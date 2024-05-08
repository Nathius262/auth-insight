# auth-insight
A web application built with Django, Auth-insight is intended to improve user authentication procedures for companies. Auth-insight seeks to address typical authentication issues including tiredness, dissatisfaction, and overload of logins by combining big data analysis and machine learning. The application includes data gathering for analysis, insights production based on machine learning categorization, and a single sign-on (SSO) mechanism for simplified authentication across various services. Ongoing authentication system optimization is ensured by constant monitoring. AuthInsight offers practical insights to enhance enterprise security and user experiences.

## Features

- Single Sign-On (SSO): Streamline user authentication across multiple organizational services with a seamless login experience.
- Big Data Integration: Collect, store, and analyze large volumes of user authentication data to gain valuable insights.
- Machine Learning Classification: Utilize machine learning algorithms to classify user activities and identify authentication-related challenges.
- Insights Generation: Generate actionable insights into common issues such as login overload, login fatigue, and login frustration.
- Continuous Monitoring: Deployed solution includes monitoring mechanisms for ongoing optimization and performance evaluation.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Nathius262/auth-insight.git
cd auth-insight
```

install dependencies
```
pip install -r requirements.txt
```

make migrations
```
python manage.py migrate
```

Run server
```
python manage.py runserver
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.


Stephan Wiefling, Paul René Jørgensen, Sigurd Thunem, and Luigi Lo
Iacono: Pump Up Password Security! Evaluating and Enhancing Risk-Based
Authentication on a Real-World Large-Scale Online Service. In: ACM
Transactions on Privacy and Security (2022). doi: [10.1145/3546069](https://doi.org/10.1145/3546069)



[Pump Up Password Security! Evaluating and Enhancing Risk-Based Authentication on a Real-World Large-Scale Online Service]: https://doi.org/10.1145/3546069
[Risk-Based Authentication (RBA)]: https://riskbasedauthentication.org
[Freeman et al. (2016)]: https://doi.org/10.14722/ndss.2016.23240
[Creative Commons Attribution 4.0 International (CC BY 4.0)]: https://creativecommons.org/licenses/by/4.0/