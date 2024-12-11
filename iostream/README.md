# B-Hydra: Устойчивая блокчейн-сеть для глобальных катастроф

B-Hydra — это децентрализованная блокчейн-система, способная функционировать в условиях глобального отключения интернета. Она обеспечивает продолжение транзакций, майнинга и работы сети благодаря технологии Device-to-Device (D2D), что делает её идеальной для использования в условиях чрезвычайных ситуаций.

---

## Ключевые особенности
1. Автономная работа:
   - Не требует подключения к централизованным серверам или глобальной сети интернет.
   - Узлы связываются друг с другом напрямую с помощью D2D (Wi-Fi Direct, Bluetooth или локальные IP-сети).

2. Стабильность сети:
   - Использует Mesh-сеть для передачи данных между узлами.
   - Гарантирует синхронизацию блокчейна даже при изоляции отдельных групп узлов.

3. Децентрализованный консенсус:
   - Реализует гибридный консенсусный алгоритм для локальной сети (например, PoW и Gossip Protocol).
   - Узлы самостоятельно находят друг друга и поддерживают работу блокчейна.

4. Поддержка майнинга:
   - Узлы продолжают добычу блоков даже в автономных условиях.
   - Энергоэффективная архитектура для работы на устройствах с ограниченными ресурсами.

5. Обеспечение безопасности:
   - Все транзакции и данные шифруются с использованием современных криптографических методов (RSA, AES).
   - Система устойчива к атакам типа Sybil благодаря механизму идентификации узлов.

6. Готовность к восстановлению:
   - После восстановления интернета система автоматически синхронизируется с глобальным блокчейном.
   - Узлы сохраняют локальные резервные копии данных.

---

## Как это работает?

1. Связь между узлами:
   - Узлы используют D2D технологии (Wi-Fi Direct, Bluetooth) для связи в условиях отсутствия интернета.
   - Mesh-сеть автоматически обнаруживает ближайших соседей.

2. Передача данных:
   - Распространение информации реализовано через Gossip Protocol, что обеспечивает высокую устойчивость сети.

3. Майнинг:
   - Локальные узлы распределяют задачи майнинга, сохраняя эффективность даже в малых сетях.

4. Синхронизация:
   - При восстановлении связи сеть автоматически синхронизирует локальные изменения с глобальным блокчейном.

---

## Цели проекта
B-Hydra была создана для обеспечения децентрализованной экономики, которая может выжить в условиях катастроф и отключения интернета. Основные цели:
- Сохранение работоспособности сети даже в экстремальных условиях.
- Поддержка микротранзакций и локального майнинга.
- Укрепление доверия к децентрализованным системам.

---

## Установка

1. Клонируйте репозиторий:
   `bash
   git clone https://github.com/username/b-hydra.git


   # B-Hydra: A Resilient Blockchain Network for Global Disasters

   B-Hydra is a decentralized blockchain system that can operate during a global internet shutdown. It ensures the continuation of transactions, mining, and network operations thanks to Device-to-Device (D2D) technology, making it ideal for use in emergency situations.

   ---

   ## Key Features
1. Autonomous Operation:
- Does not require connection to centralized servers or the global Internet.
- Nodes communicate with each other directly using D2D (Wi-Fi Direct, Bluetooth or local IP networks).

- 2. Network stability:
- Uses a mesh network to transfer data between nodes.
- Guarantees blockchain synchronization even when individual groups of nodes are isolated.

- 3. Decentralized consensus:
- Implements a hybrid consensus algorithm for the local network (e.g. PoW and Gossip Protocol).
- Nodes independently find each other and support the operation of the blockchain.

- 4. Mining support:
- Nodes continue mining blocks even in offline conditions.
- Energy-efficient architecture for operation on devices with limited resources.

- 5. Security:
- All transactions and data are encrypted using modern cryptographic methods (RSA, AES).
- The system is resistant to Sybil attacks due to the node identification mechanism.

- 6. Ready for recovery:
- Once the Internet is restored, the system automatically synchronizes with the global blockchain.
- Nodes save local backups of data.

- ---

## How does it work?

1. Communication between nodes:
- Nodes use D2D technologies (Wi-Fi Direct, Bluetooth) for communication in the absence of the Internet.
- Mesh network automatically detects the nearest neighbors.

  2. Data transmission:
- Information distribution is implemented via Gossip Protocol, which ensures high network stability.

- 3. Mining: - Local nodes distribute mining tasks, maintaining efficiency even in small networks.
 
  4. Synchr
  5. onization:
- When the connection is restored, the network automatically synchronizes local changes with the global blockchain.

- ---

## Project goals

B-Hydra was created to provide a decentralized economy that can survive disasters and internet shutdowns. The main goals are:
- Maintaining network functionality even in extreme conditions.
  - Support for microtransactions and local mining.
- Strengthening trust in decentralized systems.

- ---

## Installation

1. Clone the repository:
`bash
git clone https://github.com/username/b-hydra.git
