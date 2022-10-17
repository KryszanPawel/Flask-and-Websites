Project is part of 100 Days of Code: The Complete Python Pro Bootcamp for 2022.
During this project I have learnt a lot about using bootstrap, flask and jinja.
Website is rendered on flask server, it is styled with bootstrap framework and it works with jinja templates.
Header and footer on every site are imported by jinja and posts are automatically rendered by jinja for loop and request module. Script is downloading posts from npoint API and render them on main website.
Full content of post is accessible by clicking on header. Script moves to template site "post.html" where full post is rendered on based on id of clicked title.
Blog has fully functional navigation bar, stuck to top of website.

Update 17/10/22:
Fix of contact form: contact form sends email through smtplib module with data included in form.
Header on "/contact" endpoint changes to notify if form was sent successfully or something went wrong during posting form.
(form uses flask request method GET/POST to work)
Email is sent using smtplib, my tip is to use hotmail or outlook email as domain sent from. In other cases you woould need to change details in smtlib.SMTP method (gmail.com does not work, it doesn't allow accessing mail by 3rd party application any more.)
