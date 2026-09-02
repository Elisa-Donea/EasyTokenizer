# EasyTokenizer
**Simple BPE Tokenizer, This project is not for real-word use, it is a personal project created for practice and learning.**

Heavily inspired and informed by "_LMs Language Models are Unsupervised Multitask Learners_"[^fn], The GPT-2 Tokenizer[^fn2] as explained by _Andrej Karpathy_[^fn1] And of course "_Neural Machine Translation of Rare Words with Subword Units_"[^fn3].


### Notes

It doesn't work for languages such a chinese as the PreTokenizer will take every character as a continous token, 你好 and 我爱你 will be treated as completely different by the BPE even though they both have the 你 character.

[^fn]: Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language models are unsupervised multitask learners. OpenAI. https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf.

[^fn1]:Karpathy, A., Turgutlu, K., & Solveit. (2025, October 16). Let's build the GPT tokenizer: A complete guide to tokenization in LLMs. Fast.ai. https://www.fast.ai/posts/2025-10-16-karpathy-tokenizers.html#gpt-2-and-gpt-4-tokenizers

[^fn2]:Tiktokenizer. (n.d.). Tiktokenizer [Web application]. Retrieved September 2, 2026, from https://tiktokenizer.vercel.app/

[^fn3]: Sennrich, R., Haddow, B., & Birch, A. (2015). Neural machine translation of rare words with subword units (arXiv Preprint No. arXiv:1508.07909). arXiv. https://arxiv.org/pdf/1508.07909