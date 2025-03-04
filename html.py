<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Society Org</title>
    <style>
        
        .cover {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        .cover img {
            width: 60%;
            height: 60%;
            object-fit: cover;
            opacity: 0;
            animation: fadeInScale 2s forwards;
        }
        @keyframes fadeInScale {
            0% {
                opacity: 0;
                transform: scale(0.8);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        
        body {
            margin: 0;
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            overflow-y: auto;  
        }
        .container {
            margin-top: 20px;
            position: relative;
            z-index: 1;
        }
        .title-container {
            margin-top: 50px;
        }
        .title {
            font-size: 70px;
            font-weight: bold;
            text-transform: uppercase;
            color: white;
            display: inline-block;
            border: 4px solid white;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.5);
            box-shadow: 0 0 10px white, 0 0 20px white;
            transition: transform 0.3s;
        }
        .title:hover {
            transform: scale(1.1);
        }
        .skull {
            width: 100px;
            height: auto;
            opacity: 0.5;
            margin-top: 20px;
            animation: fadeInOut 2s infinite;
        }
        @keyframes fadeInOut {
            0%, 100% { opacity: 0; }
            50% { opacity: 0.5; }
        }
        .menu {
            margin-top: 70px;
        }

        .animated-text-container {
            position: relative;
            margin-top: 50px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
            display: inline-block;
            max-width: 80%;
        }

        .animated-text {
            font-size: 2rem;
            color: white;
            text-shadow: 0 0 15px #fff, 0 0 30px #fff;
            opacity: 0;
            transform: translateY(20px);
            animation: slideIn 2s forwards;
        }

        .description {
            font-size: 1.3rem;
            color: white;
            margin-top: 15px;
            padding: 10px;
            opacity: 0;
            animation: fadeIn 2s forwards 1s;
            text-shadow: 0 0 10px #fff, 0 0 20px #fff;
            line-height: 1.5;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        .contact-form {
            margin-top: 50px;
            opacity: 0;
            transform: translateY(50px);
            animation: slideIn 2s forwards 2s;
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 0 10px white, 0 0 20px white;
            max-width: 80%;
        }
        .contact-form input, .contact-form textarea {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            background: transparent;
            border: 1px solid white;
            color: white;
            font-size: 1rem;
            text-shadow: 0 0 5px #fff;
        }
        .contact-form input::placeholder, .contact-form textarea::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
        .contact-form button {
            background: black;
            color: white;
            border: 1px solid white;
            padding: 10px 20px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.3s, transform 0.3s;
            text-shadow: 0 0 5px #fff;
        }
        .contact-form button:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: scale(1.1);
        }

        #particles-js {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
        }
    </style>
</head>
<body>
    
    <div class="cover">
        <img src="https://cdn.discordapp.com/attachments/1345488809747284029/1345856931302215853/CF12700B-A40A-4D5E-89B0-CCCF0DB36FBE.jpg?ex=67c61271&is=67c4c0f1&hm=6faeb4a31699c90b8b9b673dcbfcde3717a338a7139ba6ddec5b4680e96458e2&" alt="Calavera 3D" alt="Portada">
    </div>

    
    <div class="container" style="display: none;">
        <div id="particles-js"></div>

        <div class="title-container">
            <h1 class="title">=777=Sct</h1>
            <img class="skull" src="https://cdn.discordapp.com/attachments/1345488809747284029/1345856931302215853/CF12700B-A40A-4D5E-89B0-CCCF0DB36FBE.jpg?ex=67c61271&is=67c4c0f1&hm=6faeb4a31699c90b8b9b673dcbfcde3717a338a7139ba6ddec5b4680e96458e2&" alt="Calavera 3D">
        </div>

        
        <div class="animated-text-container">
            <div class="animated-text">¿Qué es 777 Society?</div>
            <div class="description">
                =777= es una comunidad de Discord cuya función principal es realizar hackeos, nerfeos y defaceos a webs gubernamentales principal mente para demostrar sus graves vulnerabilidades o aveces cuando algo nos parece injusto, o abusivo haciendo cosas como filtraciones de datos en algunas de nuestras redes sociales
            </div>
        </div>

        <div class="animated-text-container">
            <div class="animated-text">Contacto</div>
            <div class="description">
                Si te interesa unirte a la comunidad, contáctanos rellenando el siguiente formulario.
            </div>
        </div>

      <div class="animated-text-container">
            <div class="animated-text">Servicios Gratuitos</div>
            <div class="description">
                
              
            </div>
        </div>
<div class="animated-text-container">
            <div class="animated-text">DDoS</div>
            <div class="description">
    contactanos, por discord para hacer ataques de DDoS https://discord.gg/z2eguphG
            </div>
        </div>
<div class="animated-text-container">
            <div class="animated-text">Defaceo/hackeo</div>
            <div class="description">
    Contactanos, por discord para Hackear/defacear una web, gubernamental o de alguien especifico
        https://discord.gg/z2eguphG
            </div>
        </div>
<div class="animated-text-container">
            <div class="animated-text">Contacto</div>
            <div class="description">
                Si te interesa unirte a la comunidad, contáctanos rellenando el siguiente formulario.
            </div>
        </div>
      <div class="animated-text-container">
            <div class="animated-text">Servicios de pago$</div>
            <div class="description">
    
            </div>
        </div>
      </div>
        </div>
      <div class="animated-text-container">
            <div class="animated-text">20€</div>
            <div class="description">
    Sacar informacion de una web como, la database, correos electronicos, documentacin oficial de identidad o filtracion de datos 
              
            </div>
        </div>
        
        <div class="contact-form">
            <input type="email" placeholder="Correo electrónico" required>
            <input type="tel" placeholder="Número de teléfono" required>
            <input type="text" placeholder="User de Discord" required>
            <button type="submit">Enviar</button>
        </div>
    </div>

    <script>
        setTimeout(() => {
            document.querySelector('.cover').style.display = 'none';
            document.querySelector('.container').style.display = 'block';
        }, 4000);
    </script>
</body>
</html>