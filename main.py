import Database as db
from flask import Flask,render_template,redirect,request,session,url_for,flash
import uuid
import core
app=Flask(__name__)
app.secret_key="SSFSSFSS"


@app.route('/',methods=['get','post'])
def login():
    if "login" in request.form:
        username=request.form['username']
        password=request.form['password']
        log_id=db.select("select * from tbl_login where username='%s'and password='%s'" %(username,password))
        if len(log_id)>0:
            session['id'] = log_id[0]['login_id']
            flash("LOGIN SUCCESSFUL")
            if log_id[0]['login_type']=='admin':
                return redirect(url_for("admin_home"))
            else:
                return redirect(url_for("doctor_home"))
        else:
            flash("UNSUCCESSFUL")
            return render_template('public/login.html')
    return render_template('public/login.html')


@app.route('/public/forgot_password',methods=['get','post'])
def forgot_password():
    if "forgot_password" in request.form:
        username=request.form['username']
        email=request.form['email']
        phone=request.form['phonenumber']
        fpass=db.select("select * from tbl_doctor inner join tbl_login using(login_id) where username='%s' and email='%s' and phone_no='%s'" %(username,email,phone))
        if len(fpass)>0:
            password=fpass[0]['password']
            return render_template('public/password_view.html',data=password)
        else:
            flash("Incorrect Data")
    return render_template('public/forgot_password.html')


@app.route('/public/password_view',methods=['get','post'])
def password_view():
    if "ok" in request.args:
        return render_template('public/login.html')
    return render_template('public/login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/admin/doctor_register/',methods=['get','post'])
def doctor_register():
    if "register" in request.form:
        docid=request.form['docid']
        fname=request.form['firstname']
        lname=request.form['lastname']
        enrollemntno=request.form['enrollmentno']
        email = request.form['email']
        phone=request.form['phonenumber']
        gender=request.form['gender']
        qualification = request.form['qualification']
        specialization=request.form['specialization']
        experience=request.form['experience']
        house=request.form['house']
        city=request.form['city']
        state=request.form['state']
        pin=request.form['pin']
        username=request.form['username']
        password=request.form['password']
        confirmpass=request.form['confirmpassword']
        chk=db.select("select username from tbl_login where username='%s'" %(username))
        if len(chk)>0:
            flash("Already Registered")
            return redirect(url_for("doctor_register"))
        else:
            if password==confirmpass:
                login_id=db.insert("insert into tbl_login(username,password,login_type)values('%s','%s','doctor')" %(username,password))
                doc_id=db.insert("insert into tbl_doctor(doc_id,login_id,fname,lname,reg_no,email,phone_no,gender,qualification,specialization,experience,house,city,state,pin)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(docid,login_id,fname,lname,enrollemntno,email,phone,gender,qualification,specialization,experience,house,city,state,pin))
            if login_id > 0:
                flash("SUCCESSFULLY REGISTERED")
            # else:
            #     print("Unsuccessful")
            else:
                flash("UNSUCCESSFUL")
            # print ("Password doesn't Match")
    return render_template('admin/doctor_register.html')


@app.route('/admin/doctor_update/',methods=['get','post'])
def doctor_update():
    if "update" in request.form:
        u_id=request.args['u_id']
        fname=request.form['firstname']
        lname=request.form['lastname']
        enrollmentno=request.form['enrollmentno']
        email=request.form['email']
        phone = request.form['phonenumber']
        gender=request.form['gender']
        qualification=request.form['qualification']
        specialization=request.form['specialization']
        experience=request.form['experience']
        house = request.form['house']
        city = request.form['city']
        state = request.form['state']
        pin = request.form['pin']
        value=db.update("update tbl_doctor set fname='%s',lname='%s',reg_no='%s',email='%s',phone_no='%s',gender='%s',qualification='%s',specialization='%s',experience='%s',house='%s',city='%s',state='%s',pin='%s' where doc_id='%s'" %(fname,lname,enrollmentno,email,phone,gender,qualification,specialization,experience,house,city,state,pin,u_id))
        flash("SUCESSFULLY UPDATED")
        return redirect(url_for("doctor_edit"))
    if "update" in request.args:
        u_id=request.args['u_id']
        s=db.select("select doc_id,fname,lname,reg_no,email,phone_no,gender,qualification,specialization,experience,house,city,state,pin from tbl_doctor where doc_id='%s'" %(u_id))
    return render_template('admin/doctor_update.html',data=s[0])


@app.route('/admin/doctor_edit',methods=['get','post'])
def doctor_edit():
    if "delete" in request.args:
        dele_id=request.args['id']
        d=db.delete("delete from tbl_doctor where login_id='%s'" %(dele_id))
        l=db.delete("delete from tbl_login where login_id='%s'" %(dele_id))
    s=db.select("select * from tbl_doctor")
    return render_template('admin/doctor_edit.html',data=s)


@app.route('/admin/doctor_view',methods=['get','post'])
def doctor_view():
    if "view" in request.args:
        v_id=request.args['v_id']
        v=db.select("select * from tbl_doctor where doc_id='%s'" %(v_id))
    return render_template('admin/doctor_view.html',data=v[0])


@app.route('/admin/patient_register',methods=['get','post'])
def patient_register():
    if "register" in request.form:
        patientid=request.form['patientid']
        fname=request.form['firstname']
        lname=request.form['lastname']
        gender=request.form['gender']
        age=request.form['age']
        phone=request.form['phonenumber']
        house=request.form['house']
        city=request.form['city']
        state=request.form['state']
        pin=request.form['pin']
        patient_id=db.insert("insert into tbl_patient(patient_id,fname,lname,gender,age,phone_no,house,city,state,pin)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(patientid,fname,lname,gender,age,phone,house,city,state,pin))
        if (patient_id>0):
            flash("SUCCESSFULLY INSERTED")
        else:
            print ("Unsuccessful")
    return render_template('admin/patient_register.html')


@app.route('/admin/patient_update',methods=['get','post'])
def patient_update():
    if "update" in request.form:
        p_id=request.args['p_id']
        fname=request.form['firstname']
        lname=request.form['lastname']
        gender=request.form['gender']
        age=request.form['age']
        phone=request.form['phonenumber']
        house=request.form['house']
        city=request.form['city']
        state=request.form['state']
        pin=request.form['pin']
        value=db.update("update tbl_patient set fname='%s',lname='%s',gender='%s',age='%s',phone_no='%s',house='%s',city='%s',state='%s',pin='%s' where patient_id='%s'" %(fname,lname,gender,age,phone,house,city,state,pin,p_id))
        flash("SUCESSFULLY UPDATED")
        return redirect(url_for("patient_view"))
    if "update" in request.args:
        p_id = request.args['p_id']
        s = db.select("select patient_id,fname,lname,gender,age,phone_no,house,city,state,pin from tbl_patient where patient_id='%s'" %(p_id))
    return render_template('admin/patient_update.html', data=s[0])


@app.route('/admin/patient_edit',methods=['get','post'])
def patient_edit():
    if "delete" in request.args:
        dele_id=request.args['id']
        d=db.delete("delete from tbl_patient where patient_id='%s'" %(dele_id))
    s=db.select("select * from tbl_patient")
    return render_template('admin/patient_edit.html',data=s)


@app.route('/admin/view_report',methods=['get','post'])
def view_report():
    value=db.select("select fname,lname,gender,age from tbl_patient")
    return render_template('admin/view_report.html',data=value[0])


@app.route('/admin/model_details',methods=['get','post'])
def model_details():
    details = core.get_model_score()
    return render_template('admin/model_details.html', model_details=details)


@app.route('/admin/train')
def train():
    details = core.train_model()
    return "ok"


@app.route('/doctor/view_patient',methods=['get','post'])
def view_patient():
    v=db.select("select * from tbl_patient")
    if "search" in request.form:

        fname=request.form['firstname']
        q = "select * from tbl_patient where fname like '%s'"  % ("%"+fname+"%")
        # print q
        v=db.select(q)

        # return render_template('doctor/view_patient.html',data=v)
    # v=db.select("select * from tbl_patient left join tbl_patient_rec using(patient_id)")
    return render_template('doctor/view_patient.html',data=v)


@app.route('/doctor/view_report')
def doctor_view_report():
    patient_id = request.args['patient_id']
    q = "select * from tbl_patient left join tbl_patient_rec using(patient_id) where patient_id='%s'" % patient_id
    res = db.select(q)
    for i in range(len(res)):
        row = res[i]
        if row['image'] != None:
            ad = core.get_ad_detection(row['image'])
            row['AD'] = ad
        res[i] = row
    return render_template('doctor/doctor_view_report.html',report = res)






    return "ok"


@app.route('/doctor/upload_mri',methods=['get','post'])
def upload_mri():
    patient_id = request.args['patient_id']
    if "upload" in request.form:
        image = request.files['scan']
        filename = "static/uploads/" + str(uuid.uuid4()) + "." +(image.filename).split(".")[-1]
        image.save(filename)
        log_id = session['id']
        description  = request.form['description']
        q = "insert into tbl_patient_rec (patient_id,date,doc_id,description,image)values('%s',curdate(),(select doc_id from tbl_doctor where login_id='%s'),'%s','%s')" % (patient_id,log_id,description,filename)
        db.insert(q)
    q = "select * from tbl_patient where patient_id='%s'" % patient_id
    res = db.select(q)
    return render_template('doctor/upload_mri.html', patient_details=res)


@app.route('/admin/admin_home')
def admin_home():
    if "id" in session:
        return render_template('admin/admin_home.html')
    else:
        return redirect(url_for('login'))


@app.route('/doctor/doctor_home')
def doctor_home():
    return render_template('doctor/doctor_home.html')


app.run(debug=True)