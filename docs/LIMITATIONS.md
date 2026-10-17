# Limitations (M07 export)

## Implemented and testable in this repository

- 4×14×n card tensor representation and core card physics primitives
- **High Card Duel**, **Mini Spades**, **Simplified Gin Rummy** environments
- Bounded **PPO/DQN** training pipeline smoke (short CPU episodes in tests)
- XAI overlay and replay/artifact **infrastructure** within tested scope
- Optional **RediAI bridge** adapters (RediAI package **not** required for default tests)

## Not demonstrated by this repository

- A universal card-playing agent or competence across arbitrary card games
- Verified transfer learning between games
- Genesis Project UNGAR frozen-core generalization (Blackjack, Hearts, Crazy Eights)
- Strong competitive performance or measured learning gains from bundled `runs/` artifacts (excluded from export)

Treat **“All card games, one brain.”** as research direction, not an accomplished result.
