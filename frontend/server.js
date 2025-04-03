const express = require('express');
const { MongoClient } = require('mongodb');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection configuration
const mongoUrl = process.env.MONGODB_URI || 'mongodb://localhost:27017';
const dbName = process.env.MONGODB_DB || 'n8n';
let db;

// Connect to MongoDB
async function connectToMongo() {
  try {
    const client = await MongoClient.connect(mongoUrl);
    db = client.db(dbName);
    console.log('Connected to MongoDB');
  } catch (error) {
    console.error('MongoDB connection error:', error);
    process.exit(1);
  }
}

connectToMongo();

// Routes
app.get('/api/topics/:inputHash', async (req, res) => {
  try {
    const { inputHash } = req.params;
    const topic = await db.collection('pillarposts').findOne({ input_hash: inputHash });
    
    if (!topic) {
      // Initialize with empty array if no document exists
      const newTopic = { input_hash: inputHash, core_topics: [] };
      await db.collection('pillarposts').insertOne(newTopic);
      return res.json(newTopic);
    }
    
    res.json(topic);
  } catch (error) {
    console.error('Error fetching topics:', error);
    res.status(500).json({ error: 'Error fetching topics' });
  }
});

app.put('/api/topics/:inputHash', async (req, res) => {
  try {
    const { inputHash } = req.params;
    const { core_topics } = req.body;
    
    const result = await db.collection('pillarposts').updateOne(
      { input_hash: inputHash },
      { 
        $set: { core_topics },
        $setOnInsert: { input_hash: inputHash }
      },
      { upsert: true }
    );
    
    res.json({ input_hash: inputHash, core_topics });
  } catch (error) {
    console.error('Error updating topics:', error);
    res.status(500).json({ error: 'Error updating topics' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
}); 