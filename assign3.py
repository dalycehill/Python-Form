#!/usr/local/bin/python3

import cgi
import MySQLdb
import MySQLdb.cursors
from wsgiref.simple_server import make_server

html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Web page</title>
            </head>

            <body>
                <p>Please fill in this form. Required fields are marked (*).</p>
                <form action="" method="POST">
                    Title*: <select name="title">
                        <option value="" selected></option>
                        <option value="Mr">Mr</option>
                        <option value="Mrs">Mrs</option>
                        <option value="Ms">Ms</option>
                        <option value="Dr">Dr</option>
                    </select><br />
                    First Name*: <input type="text" name="firstName" value="" /><br/>
                    Last Name*: <input type="text" name="lastName" value="" /><br/>
                    Street*: <input type="text" name="street" value="" /><br/>
                    City*: <input type="text" name="city" value="" /><br/>
                    Province*: <input type="text" name="province" value="" /><br/>
                    Postal Code*: <input type="text" name="postalCode" value="" /><br/>
                    Country*: <select name="country">
                        <option value="" selected></option>
                        <option value="USA">USA</option>
                        <option value="Canada">Canada</option>
                    </select><br/>
                    Phone*: <input type="text" name="phone" value="" /><br/>
                    Email*: <input type="text" name="email" value="" /><br/>
                    Newsletter: <input type="checkbox" name="newsletter" /><br/>
                    <input type="submit" name="submit" value="Submit" />
                </form>
            </body>
        </html>
        """

def app(environ, start_response):
    response = html
    if (environ['REQUEST_METHOD'] == "POST"):
        post_env = environ.copy()
        post_env["QUERY_STRING"] = ""

        post = cgi.FieldStorage(
            fp = environ["wsgi.input"],
            environ = post_env,
            keep_blank_values = True
        )

        # get the entered values
        titleVar = post["title"].value
        fNameVar = post["firstName"].value
        lNameVar = post["lastName"].value
        streetVar = post["street"].value
        cityVar = post["city"].value
        provinceVar = post["province"].value
        postalCodeVar = post["postalCode"].value
        countryVar = post["country"].value
        phoneVar = post["phone"].value
        emailVar = post["email"].value
        try:
            newsVar = post["newsletter"].value
        except:
            newsVar = "off"

        # errors
        errors = 0
        e1 = ""
        e2 = ""
        e3 = ""
        e4 = ""
        e5 = ""
        e6 = ""
        e7 = ""
        e8 = ""
        e9 = ""
        e10 = ""
        titleSelect = ""
        mrSelect = ""
        mrsSelect = ""
        msSelect = ""
        docSelect = ""
        countrySelect = ""
        usaSelect = ""
        canSelect = ""
        newsCheck = ""

        if (titleVar==""):
            errors = 1
            e1 = "<span style='color:red'>*required</span>"
        if (fNameVar==""):
            errors = 2
            e2 = "<span style='color:red'>*required</span>"
        if (lNameVar==""):
            errors = 3
            e3 = "<span style='color:red'>*required</span>"
        if (streetVar==""):
            errors = 4
            e4 = "<span style='color:red'>*required</span>"
        if (cityVar==""):
            errors = 5
            e5 = "<span style='color:red'>*required</span>"
        if (provinceVar==""):
            errors = 6
            e6 = "<span style='color:red'>*required</span>"
        if (postalCodeVar==""):
            errors = 7
            e7 = "<span style='color:red'>*required</span>"
        if (countryVar==""):
            errors = 8
            e8 = "<span style='color:red'>*required</span>"
        if (phoneVar==""):
            errors = 9
            e9 = "<span style='color:red'>*required</span>"
        if (emailVar==""):
            errors = 10
            e10 = "<span style='color:red'>*required</span>" 

        # display previously entered dropdown value
        if (titleVar == ""):
            titleSelect = "selected"
        elif (titleVar == "Mr"):
            mrSelect = "selected"
        elif (titleVar == "Mrs"):
            mrsSelect = "selected"
        elif (titleVar == "Ms"):
            msSelect = "selected"
        elif (titleVar == "Dr"):
            docSelect = "selected"

        if (countryVar == ""):
            countrySelect = "selected"
        elif (countryVar == "USA"):
            usaSelect = "selected"
        elif (countryVar == "Canada"):
            canSelect = "selected"

        if (newsVar == "on"):
            newsCheck = "checked"
        
        # redisplay form with values/error messages
        if (errors != 0):
            response = """
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Web page</title>
                    </head>

                    <body>
                        <p>Please fill in this form. Required fields are marked (*).</p>
                        <form action="" method="POST">
                            Title*: <select name="title">
                                <option value="" %s></option>
                                <option value="Mr" %s>Mr</option>
                                <option value="Mrs" %s>Mrs</option>
                                <option value="Ms" %s>Ms</option>
                                <option value="Dr" %s>Dr</option>
                            </select>%s<br />
                            First Name*: <input type="text" name="firstName" value="%s" />%s<br/>
                            Last Name*: <input type="text" name="lastName" value="%s" />%s<br/>
                            Street*: <input type="text" name="street" value="%s" />%s<br/>
                            City*: <input type="text" name="city" value="%s" />%s<br/>
                            Province*: <input type="text" name="province" value="%s" />%s<br/>
                            Postal Code*: <input type="text" name="postalCode" value="%s" />%s<br/>
                            Country*: <select name="country">
                                <option value="" %s></option>
                                <option value="USA" %s>USA</option>
                                <option value="Canada" %s>Canada</option>
                            </select>%s<br/>
                            Phone*: <input type="text" name="phone" value="%s" />%s<br/>
                            Email*: <input type="text" name="email" value="%s" />%s<br/>
                            Newsletter: <input type="checkbox" name="newsletter" %s/><br/>
                            <input type="submit" name="submit" value="Submit" />
                        </form>
                    </body>
                </html>
                """ %(titleSelect, mrSelect, mrsSelect, msSelect, docSelect, 
                    e1, fNameVar, e2, lNameVar, e3, streetVar, e4, cityVar, e5, 
                    provinceVar, e6, postalCodeVar, e7, countrySelect, usaSelect, 
                    canSelect, e8, phoneVar, e9, emailVar, e10, newsCheck)

        else:
            # insert into db
            db = MySQLdb.connect(host='localhost', port=3306, user='student', passwd='student', db='assignment3')
            cursor = db.cursor()

            sql = """INSERT INTO registered_users (
                        title, first_name, last_name, street, city, province, postal_code, country, phone, email, newsletter)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = [titleVar, fNameVar, lNameVar, streetVar, cityVar, provinceVar, postalCodeVar, countryVar, phoneVar, emailVar, newsVar]

            cursor.execute(sql, values)
            db.commit()

            # display all from db in table
            cursor.execute("SELECT * FROM registered_users")
            data = cursor.fetchall()
            response = """ <table border="" >
                    <tr>
                        <th>user_id</th>
                        <th>Title</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Street</th>
                        <th>City</th>
                        <th>Province</th>
                        <th>Postal Code</th>
                        <th>Country</th>
                        <th>Phone</th>
                        <th>Email</th>
                        <th>Newsletter</th>
                    </tr>"""

            for row in data:
                id = row[0]
                title = row[1]
                firstName = row[2]
                lastName = row[3]
                street = row[4]
                city = row[5]
                province = row[6]
                postalCode = row[7]
                country = row[8]
                phone = row[9]
                email = row[10]
                newsletter = row[11]            
                response += """
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                        </tr> 
                """  %(id, title, firstName, lastName, street, city, province, postalCode, country, phone, email, newsletter) 

            response += "</table>"
            cursor.close()
            db.close()

            import gc
            gc.collect()  

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [response.encode( )]

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Goodbye")