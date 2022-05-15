<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de gabarito</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <style>
        .marca {
            background-color: #000;
            color: #000;
        }
    </style>
</head>

<body>
    <h1 class="text-center">Diagrama de gabarito ENEM</h1>
    <p>Clique no botão abaixo para gerar os modelos de gabaritos em PNG.</p>
    <button onclick="generate()" class="btn btn-primary">Gerar gabaritos</button>

    <div class="row m-1">

        <?php
        // 600 colunas equivale a 100 gabaritos de 6 colunas (padrão ENEM)
        for ($j = 0; $j < 600; $j++) {
        ?>
            <div class="col-md-3 gabarito" id="gabarito">
                <div class="row text-center bg-white" style="border: 1px solid #000;">
                    <div class="col-md-12" style="border-bottom: 1px solid #000;">
                        <b>QUESTÃO/RESPOSTA</b>
                    </div>
                    <?php
                    for ($i = 0; $i < 15; $i++) {
                        $marca = rand(0, 4);
                    ?>
                        <div class="col-md-12">
                            <div class="row">
                                <div class="col-md-2 p-2" style="border-right: 1px solid #000;">
                                    <b style="font-size: 1.2em;"><?= ($i + 1) ?></b>
                                </div>
                                <div class="col-md-2 p-2">
                                    <b class="<?= ($marca === 0 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 1.2em; padding: 3px 10px 3px 10px;">A</b>
                                </div>
                                <div class="col-md-2 p-2">
                                    <b class="<?= ($marca === 1 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 1.2em; padding: 3px 10px 3px 10px;">B</b>
                                </div>
                                <div class="col-md-2 p-2">
                                    <b class="<?= ($marca === 2 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 1.2em; padding: 3px 10px 3px 10px;">C</b>
                                </div>
                                <div class="col-md-2 p-2">
                                    <b class="<?= ($marca === 3 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 1.2em; padding: 3px 10px 3px 10px;">D</b>
                                </div>
                                <div class="col-md-2 p-2">
                                    <b class="<?= ($marca === 4 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 1.2em; padding: 3px 10px 3px 10px;">E</b>
                                </div>
                            </div>
                        </div>
                    <?php
                    }
                    ?>
                </div>
            </div>
        <?php
        }
        ?>


    </div>

    <script src="node_modules/dom-to-image/dist/dom-to-image.min.js"></script>
    <script>
        console.log('Abrindo página inicial...');

        var gabaritos = document.getElementsByClassName('gabarito');
        var qtd = gabaritos.length;
        var i = 0;

        function generate() {

            console.log('Gerando gabarito.....');
            // setTimeout(() => {
            domtoimage
                .toBlob(gabaritos[i])
                .then(function(blob) {
                    url = window.URL.createObjectURL(blob);
                    var a = document.createElement("a");
                    a.style = "display: none";
                    document.body.appendChild(a);
                    a.href = url;
                    a.download = 'blog.png';
                    a.click();
                    window.URL.revokeObjectURL(url);

                    console.log('gabarito: ' + i);
                    i++;
                    if (i < qtd)
                        generate();
                });
            // }, 1000);
        }
    </script>
</body>

</html>