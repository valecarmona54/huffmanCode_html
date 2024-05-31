document.addEventListener('DOMContentLoaded', function() {
    const textoInput = document.getElementById('texto');
    const botonCompress = document.querySelector('.btn-compress');
    const textoComprimidoOutput = document.getElementById('texto_comprimido');
    const diccionarioOutput = document.getElementById('diccionario');
    const botonDecompress = document.querySelector('.btn-decompress');
    const textoDescomprimidoOutput = document.getElementById('texto_descomprimido');

    botonDecompress.disabled = true;

    function comprimirTexto(texto) {
        fetch('/compress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ texto: texto })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            textoComprimidoOutput.value = data.texto_comprimido;
            diccionarioOutput.textContent = JSON.stringify(data.diccionario, null, 2);
            botonDecompress.disabled = false;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ha ocurrido un error al comprimir el texto.');
        });
    }

    function descomprimirTexto() {
        const textoComprimido = textoComprimidoOutput.value.trim();
        const diccionario = JSON.parse(diccionarioOutput.textContent.trim());
        if (textoComprimido !== '') {
            fetch('/decompress', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ texto: textoComprimido, diccionario: diccionario })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    return;
                }
                textoDescomprimidoOutput.value = data.texto_descomprimido;
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Ha ocurrido un error al descomprimir el texto.');
            });
        } else {
            alert('Por favor, comprime un texto antes de intentar descomprimirlo.');
        }
    }

    function onClickCompress() {
        const texto = textoInput.value.trim();
        if (texto !== '') {
            comprimirTexto(texto);
        } else {
            alert('Por favor ingresa un texto antes de comprimir.');
        }
    }

    function copiarDiccionario() {
        const diccionario = diccionarioOutput.textContent;
        navigator.clipboard.writeText(diccionario).then(function() {
            alert('Diccionario copiado al portapapeles');
        }, function() {
            alert('Error al copiar el diccionario');
        });
    }

    botonCompress.addEventListener('click', onClickCompress);
    botonDecompress.addEventListener('click', descomprimirTexto);
    window.copiarDiccionario = copiarDiccionario;
});
