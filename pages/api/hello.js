
export default (req, res) => {
  const tabela = fetch(
    'https://api.airtable.com/v0/appkYesjT7j819rOp/Hospitais?maxRecords=3&view=Hospitais',
    { headers: 'Authorization: Bearer keyejuwdVkKLST1H0' }
  );
  const data = tabela.json();
  res.status(200).json('oi');
  }
