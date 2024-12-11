document.getElementById("saveNoteButton").addEventListener("click", function () {
    const noteId = document.getElementById("noteId").value;
    const titulo = document.getElementById("titulo").value;
    const contenido = document.getElementById("contenido").value;
    

    fetch("update-note/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: JSON.stringify({
            note_id: noteId,
            titulo: titulo,
            contenido: contenido,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.error) {
                document.getElementById("errorMessage").innerText = data.error;
                document.getElementById("errorMessage").style.display = "block";
            } else {
                alert("Nota actualizada correctamente");
                window.location.reload(); // Recargar la página para reflejar cambios
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("Ocurrió un error inesperado.");
        });
});
