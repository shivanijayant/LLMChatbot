OPENAI_API_KEY = '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'
PINECONE_API_KEY = '67fde080-d506-46df-8984-57ca36c3a298'

import pinecone_datasets
dataset = pinecone_datasets.load_dataset('wikipedia-simple-text-embedding-ada-002-100K')

# drop metadata column and renamed blob to metadata
dataset.documents.drop(['metadata'], axis=1, inplace=True)
dataset.documents.rename(columns={'blob': 'metadata'}, inplace=True)

# sample 30k documents
dataset.documents.drop(dataset.documents.index[30_000:], inplace=True)