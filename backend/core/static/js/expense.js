const currentScript = document.currentScript
const data = JSON.parse(currentScript.dataset.tokens)
const { csrf } = data

const headers = { "Content-Type": "application/json", "X_CSRFToken": csrf }

const url = '/api/v1/expenses'

const getItems = () => ({
  items: [],
  editItem: {},
  isOpen: false,

  // computed
  total: function() {
    return this.items.reduce((acc, item) => {
      return acc + parseFloat(item.value, 2)
    }, 0).toFixed(2)
  },

  init() {
    this.getData()
  },

  getData() {
    axios.get(url)
      .then(response => {
        this.items = response.data.map(item => ({ ...item, isEdit: false }))
      })
  },

  openModal() {
    this.isOpen = true
  },

  resetForm() {
    this.editItem = {}
    this.isOpen = false
  },

  getItem(item) {
    item.isEdit = true
    this.editItem = { ...item }
  },

  cancelItem(item) {
    item.isEdit = false
    this.editItem = { ...item }
  },

  saveData() {
    if (!this.editItem.id) {
      this.addItem(url)
    } else {
      this.updateItem(url)
    }
  },

  addItem(url) {
    const bodyData = { ...this.editItem }

    axios.post(url, bodyData, { headers })
      .then(response => {
        // this.items = this.items.unshift(response.data)

        // Adiciona o item no começo do array.
        // this.items = [response.data, ...this.items]

        // ou

        // Adiciona o item no final do array.
        this.items = [...this.items, response.data]

        this.resetForm()
      })
  },

  updateItem(url) {
    const id = this.editItem.id
    // Remove o id e associa o restante a bodyData
    const { id: _, ...bodyData } = this.editItem

    axios.patch(`${url}/${id}`, bodyData, { headers })
      .then(response => {
        this.updateItemInList(response.data)

        // ou
        // Atualiza a lista inteira, e mantem a ordem correta dos dados vindo do backend.
        // this.getData()

        this.resetForm()
      })
  },

  updateItemInList(updatedItem) {
    const items = [...this.items]
    const index = items.findIndex(p => p.id == updatedItem.id)
    items[index] = updatedItem // atualiza o item selecionado.
    this.items = items
  },

  deleteItem(item, index) {
    axios.delete(`${url}/${item.id}`, { headers })
      .then(response => {
        // Caso não use o index, então precisa localizá-lo.
        // const index = this.items.findIndex(p => p.id == item.id)
        this.items.splice(index, 1)
      })
  }
})