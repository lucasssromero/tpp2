<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio Beat</title>
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            margin: 0;
            padding: 0;
            background: url('https://source.unsplash.com/1600x900/?music') no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .content {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            font-size: 2.5rem;
            margin: 0 0 20px 0;
        }
        iframe {
            width: 100%;
            height: 400px;
            border: none;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Bienvenido a la mejor radio que</h1>
        <p>Tu estación de música favorita</p>
        <iframe src="https://zeno.fm/player/musica-buena-wefd" allow="autoplay"></iframe>
    </div>
</body>
</html>
