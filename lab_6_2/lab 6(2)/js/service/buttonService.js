class ButtonService {

    createButton(parent, button) {
        this.button = document.createElement("button");

        this.button.className = button.getClassName();
        this.button.textContent = button.getText();
        this.button.style.width = `${button.getWidth()}px`;
        this.button.style.height = `${button.getHeight()}px`;
        this.button.style.backgroundColor = button.getBackgroundColor();

        parent.append(this.button);

        return this.button;
    }

    deleteButton(button) {
        button.parentNode.removeChild(button);
    }

}