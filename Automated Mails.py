#import the following
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

#initialize connection to our email server, for this we will use the gmail
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

#Login with your email and password
smtp.login('YourMail.gmail.com', 'Your Password')



#send your email to the recipient
def message(subject= "Python Notification",
            text="", img=None,
             attachment=None):

    # build message contents
    msg = MIMEMultipart()
      
    # Add Subject
    msg['Subject'] = subject  
      
    # Add text contents
    msg.attach(MIMEText(text))  


    # Check if we have anything
    # given in the img parameter
    if img is not None:
        #check whether we have the lists of images
        if type (img) is not list:
            # if it is not a list then make it one
            img= [img]

    # Now you iterate through the list
    for one_img in img:
        #read the image binary data
        img_data = open(one_img, 'rb').read()
    # Attach the image data tothe MIMWMultipar
    #using MIMEImage, we add the given fil 
    msg.attach(MIMEImage(img_data,
                        name=os.path.basename(one_img)))

    # We do the same for
        # attachments as we did for images
    if attachment is not None:

     # Check whether we have the
        # lists of attachments or not!
        if type(attachment) is not list:
            
              # if it isn't a list, make it one
            attachment = [attachment]  
  
        for one_attachment in attachment:

            with open(one_attachment, 'rb') as f:

                # read in the attachement
                # using MIMEApplication
                file = MIMEApplication(
		            f.read(), name=os.path.basename(one_attachment)
	)
            file['Content-Disposition'] = f'attachment; \
            filename="{os.path.basename(one_attachment)}"'

            # At last, add the attachment to our message object
            msg.attach(file)
    return msg 

	

    
          
# Call the message function
msg = message("Good!", "Hi there!") 


                    



# Make a list of emails where you want to send the mail

to = ["bolutifeemmit@gmail.com", "topherowens15@gmail.com", "abc@gmail.com"]
# Provide some data to the send mail function 
smtp.sendmail(from_addr="stevieemmit@gmail.com",
			to_addrs=to, msg=msg.as_string())
smtp.quit()

