<!DOCTYPE html>
<html>

<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-M4G4CJ7');</script>
<!-- End Google Tag Manager -->
    <title>
        Contact
    </title>
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .mymsg{
            font-size: 1vw;
            margin: auto;
            margin-top:35px;
            width:90%;
            text-align: center;
            color: rgb(111, 9, 158);
            font-family:'Alexandria';
        }

        @media screen and (max-width: 600px) {
            .mymsg{
                font-size: 2vh;
            }
        }

    </style>
</head>

<body style="background-color:rgb(228, 205, 250)">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M4G4CJ7"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
    <div class="banner" id="banner">
        <img class="bannerpic" src="flowerbanner2.jpg">
        <div>CRAFTUITY</div>
        <a class="cart" href="cart.html"><span class="cartnumber" id="cartnumber">0</span><img src="32x32.jpg"></a>
    </div>

    <div class="topnav" id="myTopnav">
        <a href="home.html">Home</a>
        <a href="shop.html">Shop</a>
        <a href="contact.html" class="active">Contact</a>
        <a href="about.html">About</a>
    </div>
    
    <p class="mymsg">Thank you for your message! We will email you soon!</p>
    <p>
<?php

$name = $_POST['firstname'];
$textinput = $_POST['subject'];
$youremail = $_POST['youremail'];

$textinput = $textinput . "\nfrom: " . $youremail;

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

$headers = "From: contact@craftuity.com";

// send email
mail("craftuitycrafts@gmail.com","new message from $name",$textinput,$headers);
?>
</p>
</body>

</html>
